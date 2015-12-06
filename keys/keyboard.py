from ctypes.util import find_library
import ctypes as ct

from .constants import KEY_MAPPING, MODIFIERS, SHIFT_KEYS

x11 = ct.cdll.LoadLibrary(find_library("X11"))
display = x11.XOpenDisplay(None)

class KeyBoard():
    # this will hold the keyboard state.  32 bytes, with each
    # bit representing the state for a single key.
    keyboard = (ct.c_char * 32)()

    last_pressed = set()
    last_pressed_adjusted = set()
    last_modifier_state = {}
    caps_lock_state = 0


    def fetch_keys_raw(self):
        x11.XQueryKeymap(display, self.keyboard)
        return self.keyboard

    def fetch_keys(self):

        keypresses_raw = self.fetch_keys_raw()

        # check modifier states (ctrl, alt, shift keys)
        modifier_state = {}
        # for mod, (i, byte) in modifiers.iteritems():
        # for mod, (i, byte) in modifiers:
        for mod, value in MODIFIERS.items():
            i, byte = value
            modifier_state[mod] = bool(ord(keypresses_raw[i]) & byte)

        # shift pressed?
        shift = 0
        for i, byte in SHIFT_KEYS:
            if ord(keypresses_raw[i]) & byte:
                shift = 1
                break

        # caps lock state
        if ord(keypresses_raw[8]) & 4: self.caps_lock_state = int(not self.caps_lock_state)


        # aggregate the pressed keys
        pressed = []
        for i, k in enumerate(keypresses_raw):
            o = ord(k)
            if o:
                for byte,key in KEY_MAPPING.get(i, {}).items():
                    if byte & o:
                        if isinstance(key, tuple): key = key[shift or self.caps_lock_state]
                        pressed.append(key)


        tmp = pressed
        pressed = list(set(pressed).difference(self.last_pressed))
        state_changed = tmp != self.last_pressed and (pressed or self.last_pressed_adjusted)
        self.last_pressed = tmp
        self.last_pressed_adjusted = pressed

        if pressed: pressed = pressed[0]
        else: pressed = None

        state_changed = self.last_modifier_state and (state_changed or modifier_state != self.last_modifier_state)
        self.last_modifier_state = modifier_state

        return state_changed, modifier_state, pressed


