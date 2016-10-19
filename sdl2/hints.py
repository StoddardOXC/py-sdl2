from ctypes import CFUNCTYPE, c_int, c_char_p, c_void_p
from .dll import _bind
from .stdinc import SDL_bool

__all__ = ["SDL_HINT_FRAMEBUFFER_ACCELERATION", "SDL_HINT_RENDER_DRIVER",
           "SDL_HINT_RENDER_OPENGL_SHADERS", "SDL_HINT_RENDER_SCALE_QUALITY",
           "SDL_HINT_RENDER_VSYNC", "SDL_HINT_VIDEO_X11_XVIDMODE",
           "SDL_HINT_VIDEO_X11_XINERAMA", "SDL_HINT_VIDEO_X11_XRANDR",
           "SDL_HINT_GRAB_KEYBOARD", "SDL_HINT_VIDEO_MINIMIZE_ON_FOCUS_LOSS",
           "SDL_HINT_IDLE_TIMER_DISABLED", "SDL_HINT_ORIENTATIONS",
           "SDL_HINT_XINPUT_ENABLED", "SDL_HINT_GAMECONTROLLERCONFIG",
           "SDL_HINT_ALLOW_TOPMOST", "SDL_HINT_DEFAULT", "SDL_HINT_NORMAL",
           "SDL_HINT_OVERRIDE", "SDL_HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS",
           "SDL_HINT_VIDEO_HIGHDPI_DISABLED",
           "SDL_HINT_ACCELEROMETER_AS_JOYSTICK",
           "SDL_HINT_MAC_CTRL_CLICK_EMULATE_RIGHT_CLICK",
           "SDL_HINT_RENDER_DIRECT3D_THREADSAFE",
           "SDL_HINT_VIDEO_FULLSCREEN_SPACES",
           "SDL_HINT_MOUSE_RELATIVE_MODE_WARP",
           "SDL_HINT_VIDEO_WIN_D3DCOMPILER",
           "SDL_HINT_VIDEO_WINDOW_SHARE_PIXEL_FORMAT",
           "SDL_HINT_VIDEO_ALLOW_SCREENSAVER",
           "SDL_HINT_VIDEO_MAC_FULLSCREEN_SPACES",
           "SDL_HINT_RENDER_DIRECT3D11_DEBUG",
           "SDL_HINT_WINRT_PRIVACY_POLICY_URL",
           "SDL_HINT_WINRT_PRIVACY_POLICY_LABEL",
           "SDL_HINT_WINRT_HANDLE_BACK_BUTTON",
           "SDL_HINT_WINDOW_FRAME_USABLE_WHILE_CURSOR_HIDDEN",
           "SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP",
           "SDL_HINT_ANDROID_APK_EXPANSION_MAIN_FILE_VERSION",
           "SDL_HINT_ANDROID_APK_EXPANSION_PATCH_FILE_VERSION",
           "SDL_HINT_XINPUT_USE_OLD_JOYSTICK_MAPPING",
           "SDL_HINT_IME_INTERNAL_EDITING",
           "SDL_HINT_EMSCRIPTEN_KEYBOARD_ELEMENT",
           "SDL_HINT_NO_SIGNAL_HANDLERS",
           "SDL_HINT_ANDROID_SEPARATE_MOUSE_AND_TOUCH",
           "SDL_HINT_THREAD_STACK_SIZE",
           "SDL_HINT_MAC_BACKGROUND_APP",
           "SDL_HINT_WINDOWS_NO_CLOSE_ON_ALT_F4",
           "SDL_HINT_VIDEO_X11_NET_WM_PING",
           "SDL_HINT_MOUSE_FOCUS_CLICKTHROUGH",
           "SDL_HINT_APPLE_TV_CONTROLLER_UI_EVENTS",
           "SDL_HINT_APPLE_TV_REMOTE_ALLOW_ROTATION",
           "SDL_HINT_BMP_SAVE_LEGACY_FORMAT",
           "SDL_HINT_WINDOWS_DISABLE_THREAD_NAMING",
           "SDL_HINT_RPI_VIDEO_LAYER",
           "SDL_HintPriority", "SDL_SetHintWithPriority", "SDL_SetHint",
           "SDL_GetHint", "SDL_GetHintBoolean", "SDL_ClearHints"]

SDL_HINT_FRAMEBUFFER_ACCELERATION = b"SDL_FRAMEBUFFER_ACCELERATION"
SDL_HINT_RENDER_DRIVER = b"SDL_RENDER_DRIVER"
SDL_HINT_RENDER_OPENGL_SHADERS = b"SDL_RENDER_OPENGL_SHADERS"
SDL_HINT_RENDER_SCALE_QUALITY = b"SDL_RENDER_SCALE_QUALITY"
SDL_HINT_RENDER_VSYNC = b"SDL_RENDER_VSYNC"
SDL_HINT_VIDEO_X11_XVIDMODE = b"SDL_VIDEO_X11_XVIDMODE"
SDL_HINT_VIDEO_X11_XINERAMA = b"SDL_VIDEO_X11_XINERAMA"
SDL_HINT_VIDEO_X11_XRANDR = b"SDL_VIDEO_X11_XRANDR"
SDL_HINT_GRAB_KEYBOARD = b"SDL_GRAB_KEYBOARD"
SDL_HINT_VIDEO_MINIMIZE_ON_FOCUS_LOSS = b"SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS"
SDL_HINT_VIDEO_FULLSCREEN_SPACES = b"SDL_VIDEO_FULLSCREEN_SPACES"
SDL_HINT_IDLE_TIMER_DISABLED = b"SDL_IOS_IDLE_TIMER_DISABLED"
SDL_HINT_ORIENTATIONS = b"SDL_IOS_ORIENTATIONS"
SDL_HINT_ACCELEROMETER_AS_JOYSTICK = b"SDL_ACCELEROMETER_AS_JOYSTICK"
SDL_HINT_XINPUT_ENABLED = b"SDL_XINPUT_ENABLED"
SDL_HINT_GAMECONTROLLERCONFIG = b"SDL_GAMECONTROLLERCONFIG"
SDL_HINT_ALLOW_TOPMOST = b"SDL_ALLOW_TOPMOST"
SDL_HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS = b"SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"
SDL_HINT_TIMER_RESOLUTION = b"SDL_TIMER_RESOLUTION"
SDL_HINT_VIDEO_HIGHDPI_DISABLED = b"SDL_VIDEO_HIGHDPI_DISABLED"
SDL_HINT_MAC_CTRL_CLICK_EMULATE_RIGHT_CLICK = b"SDL_MAC_CTRL_CLICK_EMULATE_RIGHT_CLICK"
SDL_HINT_RENDER_DIRECT3D_THREADSAFE = b"SDL_RENDER_DIRECT3D_THREADSAFE"
SDL_HINT_MOUSE_RELATIVE_MODE_WARP = b"SDL_MOUSE_RELATIVE_MODE_WARP"
SDL_HINT_VIDEO_WINDOW_SHARE_PIXEL_FORMAT = b"SDL_VIDEO_WINDOW_SHARE_PIXEL_FORMAT"
SDL_HINT_VIDEO_ALLOW_SCREENSAVER = b"SDL_VIDEO_ALLOW_SCREENSAVER"
SDL_HINT_VIDEO_MAC_FULLSCREEN_SPACES = b"SDL_VIDEO_MAC_FULLSCREEN_SPACES"
SDL_HINT_VIDEO_WIN_D3DCOMPILER = b"SDL_VIDEO_WIN_D3DCOMPILER"
SDL_HINT_RENDER_DIRECT3D11_DEBUG = b"SDL_RENDER_DIRECT3D11_DEBUG"
SDL_HINT_WINRT_PRIVACY_POLICY_URL = b"SDL_WINRT_PRIVACY_POLICY_URL"
SDL_HINT_WINRT_PRIVACY_POLICY_LABEL = b"SDL_WINRT_PRIVACY_POLICY_LABEL"
SDL_HINT_WINRT_HANDLE_BACK_BUTTON = b"SDL_WINRT_HANDLE_BACK_BUTTON"
SDL_HINT_WINDOW_FRAME_USABLE_WHILE_CURSOR_HIDDEN = b"SDL_WINDOW_FRAME_USABLE_WHILE_CURSOR_HIDDEN"
SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP = b"SDL_WINDOWS_ENABLE_MESSAGELOOP"
SDL_HINT_ANDROID_APK_EXPANSION_MAIN_FILE_VERSION = b"SDL_ANDROID_APK_EXPANSION_MAIN_FILE_VERSION"
SDL_HINT_ANDROID_APK_EXPANSION_PATCH_FILE_VERSION = b"SDL_ANDROID_APK_EXPANSION_PATCH_FILE_VERSION"
SDL_HINT_XINPUT_USE_OLD_JOYSTICK_MAPPING = b"SDL_XINPUT_USE_OLD_JOYSTICK_MAPPING"
SDL_HINT_IME_INTERNAL_EDITING = b"SDL_IME_INTERNAL_EDITING"
SDL_HINT_ANDROID_SEPARATE_MOUSE_AND_TOUCH = b"SDL_ANDROID_SEPARATE_MOUSE_AND_TOUCH"
SDL_HINT_EMSCRIPTEN_KEYBOARD_ELEMENT = b"SDL_EMSCRIPTEN_KEYBOARD_ELEMENT"
SDL_HINT_NO_SIGNAL_HANDLERS = b"SDL_NO_SIGNAL_HANDLERS"
SDL_HINT_THREAD_STACK_SIZE = b"SDL_THREAD_STACK_SIZE"
SDL_HINT_MAC_BACKGROUND_APP = b"SDL_MAC_BACKGROUND_APP"
SDL_HINT_WINDOWS_NO_CLOSE_ON_ALT_F4 = b"SDL_WINDOWS_NO_CLOSE_ON_ALT_F4"
SDL_HINT_VIDEO_X11_NET_WM_PING = b"SDL_VIDEO_X11_NET_WM_PING"
SDL_HINT_APPLE_TV_CONTROLLER_UI_EVENTS = b"SDL_APPLE_TV_CONTROLLER_UI_EVENTS"
SDL_HINT_APPLE_TV_REMOTE_ALLOW_ROTATION = b"SDL_APPLE_TV_REMOTE_ALLOW_ROTATION"
SDL_HINT_MOUSE_FOCUS_CLICKTHROUGH = b"SDL_MOUSE_FOCUS_CLICKTHROUGH"
SDL_HINT_BMP_SAVE_LEGACY_FORMAT = b"SDL_BMP_SAVE_LEGACY_FORMAT"
SDL_HINT_WINDOWS_DISABLE_THREAD_NAMING = b"SDL_WINDOWS_DISABLE_THREAD_NAMING"
SDL_HINT_RPI_VIDEO_LAYER = b"SDL_RPI_VIDEO_LAYER"

SDL_HINT_DEFAULT = 0
SDL_HINT_NORMAL = 1
SDL_HINT_OVERRIDE = 2
SDL_HintPriority = c_int
SDL_SetHintWithPriority = _bind("SDL_SetHintWithPriority", [c_char_p, c_char_p, SDL_HintPriority], SDL_bool)
SDL_SetHint = _bind("SDL_SetHint", [c_char_p, c_char_p], SDL_bool)
SDL_GetHint = _bind("SDL_GetHint", [c_char_p], c_char_p)
SDL_GetHintBoolean = _bind("SDL_GetHintBoolean", [c_char_p, SDL_bool], SDL_bool)
SDL_ClearHints = _bind("SDL_ClearHints")
SDL_HintCallback = CFUNCTYPE(None, c_void_p, c_char_p, c_char_p, c_char_p)
SDL_AddHintCallback = _bind("SDL_AddHintCallback", [c_char_p, SDL_HintCallback, c_void_p])
SDL_DelHintCallback = _bind("SDL_DelHintCallback",[c_char_p, SDL_HintCallback, c_void_p])
