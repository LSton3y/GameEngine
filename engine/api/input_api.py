from enum import Enum
import pygame

from engine.core.game import Game


class Keys(Enum):
    """Enum of keybinds"""

    # Control Keys
    Backspace = pygame.K_BACKSPACE
    Tab = pygame.K_TAB
    Clear = pygame.K_CLEAR
    Return = pygame.K_RETURN
    Pause = pygame.K_PAUSE
    Escape = pygame.K_ESCAPE
    Space = pygame.K_SPACE
    Delete = pygame.K_DELETE

    # Symbols & Punctuation
    Exclaim = pygame.K_EXCLAIM
    Quotedbl = pygame.K_QUOTEDBL
    Hash = pygame.K_HASH
    Dollar = pygame.K_DOLLAR
    Ampersand = pygame.K_AMPERSAND
    Quote = pygame.K_QUOTE
    Leftparen = pygame.K_LEFTPAREN
    Rightparen = pygame.K_RIGHTPAREN
    Asterisk = pygame.K_ASTERISK
    Plus = pygame.K_PLUS
    Comma = pygame.K_COMMA
    Minus = pygame.K_MINUS
    Period = pygame.K_PERIOD
    Slash = pygame.K_SLASH
    Colon = pygame.K_COLON
    Semicolon = pygame.K_SEMICOLON
    Less = pygame.K_LESS
    Equals = pygame.K_EQUALS
    Greater = pygame.K_GREATER
    Question = pygame.K_QUESTION
    At = pygame.K_AT
    Leftbracket = pygame.K_LEFTBRACKET
    Backslash = pygame.K_BACKSLASH
    Rightbracket = pygame.K_RIGHTBRACKET
    Caret = pygame.K_CARET
    Underscore = pygame.K_UNDERSCORE
    Backquote = pygame.K_BACKQUOTE

    # Numbers
    Num_0 = pygame.K_0
    Num_1 = pygame.K_1
    Num_2 = pygame.K_2
    Num_3 = pygame.K_3
    Num_4 = pygame.K_4
    Num_5 = pygame.K_5
    Num_6 = pygame.K_6
    Num_7 = pygame.K_7
    Num_8 = pygame.K_8
    Num_9 = pygame.K_9

    # Alphabet
    A = pygame.K_a
    B = pygame.K_b
    C = pygame.K_c
    D = pygame.K_d
    E = pygame.K_e
    F = pygame.K_f
    G = pygame.K_g
    H = pygame.K_h
    I = pygame.K_i
    J = pygame.K_j
    K = pygame.K_k
    L = pygame.K_l
    M = pygame.K_m
    N = pygame.K_n
    O = pygame.K_o
    P = pygame.K_p
    Q = pygame.K_q
    R = pygame.K_r
    S = pygame.K_s
    T = pygame.K_t
    U = pygame.K_u
    V = pygame.K_v
    W = pygame.K_w
    X = pygame.K_x
    Y = pygame.K_y
    Z = pygame.K_z

    # Keypad Keys
    Kp0 = pygame.K_KP0
    Kp1 = pygame.K_KP1
    Kp2 = pygame.K_KP2
    Kp3 = pygame.K_KP3
    Kp4 = pygame.K_KP4
    Kp5 = pygame.K_KP5
    Kp6 = pygame.K_KP6
    Kp7 = pygame.K_KP7
    Kp8 = pygame.K_KP8
    Kp9 = pygame.K_KP9
    Kp_period = pygame.K_KP_PERIOD
    Kp_divide = pygame.K_KP_DIVIDE
    Kp_multiply = pygame.K_KP_MULTIPLY
    Kp_minus = pygame.K_KP_MINUS
    Kp_plus = pygame.K_KP_PLUS
    Kp_enter = pygame.K_KP_ENTER
    Kp_equals = pygame.K_KP_EQUALS

    # Navigation & Function Keys
    Up = pygame.K_UP
    Down = pygame.K_DOWN
    Right = pygame.K_RIGHT
    Left = pygame.K_LEFT
    Insert = pygame.K_INSERT
    Home = pygame.K_HOME
    End = pygame.K_END
    Pageup = pygame.K_PAGEUP
    Pagedown = pygame.K_PAGEDOWN
    
    # F-Keys
    F1 = pygame.K_F1
    F2 = pygame.K_F2
    F3 = pygame.K_F3
    F4 = pygame.K_F4
    F5 = pygame.K_F5
    F6 = pygame.K_F6
    F7 = pygame.K_F7
    F8 = pygame.K_F8
    F9 = pygame.K_F9
    F10 = pygame.K_F10
    F11 = pygame.K_F11
    F12 = pygame.K_F12
    F13 = pygame.K_F13
    F14 = pygame.K_F14
    F15 = pygame.K_F15

    # Modifiers & System Keys
    Numlock = pygame.K_NUMLOCK
    Capslock = pygame.K_CAPSLOCK
    Scrollock = pygame.K_SCROLLOCK
    Rshift = pygame.K_RSHIFT
    Lshift = pygame.K_LSHIFT
    Rctrl = pygame.K_RCTRL
    Lctrl = pygame.K_LCTRL
    Ralt = pygame.K_RALT
    Lalt = pygame.K_LALT
    Rmeta = pygame.K_RMETA
    Lmeta = pygame.K_LMETA
    Lsuper = pygame.K_LSUPER
    Rsuper = pygame.K_RSUPER
    
    # UI & Media Keys
    Mode = pygame.K_MODE
    Help = pygame.K_HELP
    Print = pygame.K_PRINT
    Sysreq = pygame.K_SYSREQ
    Break = pygame.K_BREAK
    Menu = pygame.K_MENU
    Power = pygame.K_POWER
    Euro = pygame.K_EURO
    Ac_back = pygame.K_AC_BACK


class Mouse(Enum):
    """Enum of mouse buttons"""

    # Standard Click Buttons
    Left = 1
    Middle = 2
    Right = 3
    
    # Scroll Wheel States
    Scroll_up = 4
    Scroll_down = 5
    
    # Extended Side Buttons
    X1 = 6  # Often "Back" navigation
    X2 = 7  # Often "Forward" navigation



def key_pressed(key: Keys):
    """Checks if a key has been pressed"""
    return Game.instance().input_manager.is_key_pressed(key.value)


def key_down(key: Keys):
    """Checks if a key is down"""
    return Game.instance().input_manager.is_key_down(key.value)


def key_released(key: Keys):
    """Checks is a key has been released"""
    return Game.instance().input_manager.is_key_released(key.value)



def mouse_pressed(mouse_button: Mouse):
    """Checks if a mouse button has been pressed"""
    return Game.instance().input_manager.is_mouse_pressed(mouse_button.value)


def mouse_down(mouse_button: Mouse):
    """Checks if a mouse button is down"""
    return Game.instance().input_manager.is_mouse_down(mouse_button.value)


def mouse_released(mouse_button: Mouse):
    """Checks if a mouse button has been released"""
    return Game.instance().input_manager.is_mouse_released(mouse_button.value)



def action_pressed(action: str):
    """Checks if an action has been pressed"""
    return Game.instance().system_manager.input_system.is_action_pressed(action)


def action_down(action: str):
    """Checks if an action is down"""
    return Game.instance().system_manager.input_system.is_action_down(action)


def action_released(action: str):
    """Checks if an action has been released"""
    return Game.instance().system_manager.input_system.is_action_released(action)