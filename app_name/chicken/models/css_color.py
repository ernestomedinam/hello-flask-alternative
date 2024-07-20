from typing import Self
from app_name.base.models.base import BaseEnum
from app_name.utils.thc import snake_to_lowercase

class CSSColor(BaseEnum):
    ALICE_BLUE = ("aliceblue", "#f0f8ff")
    ANTIQUEWHITE = ("antiquewhite", "#faebd7")
    AQUA = ("aqua", "#00ffff")
    AQUAMARINE = ("aquamarine", "#7fffd4")
    AZURE = ("azure", "#f0ffff")
    BEIGE = ("beige", "#f5f5dc")
    BISQUE = ("bisque", "#ffe4c4")
    BLACK = ("black", "#000000")
    BLANCHED_ALMOND = ("blanchedalmond", "#ffebcd")
    BLUE = ("blue", "#0000ff")
    BLUE_VIOLET = ("blueviolet", "#8a2be2")
    BROWN = ("brown", "#a52a2a")
    BURLYWOOD = ("burlywood", "#deb887")
    CADET_BLUE = ("cadetblue", "#5f9ea0")
    CHARTREUSE = ("chartreuse", "#7fff00")
    CHOCOLATE = ("chocolate", "#d2691e")
    CORAL = ("coral", "#ff7f50")
    CORNFLOWER_BLUE = ("cornflowerblue", "#6495ed")
    CORNSILK = ("cornsilk", "#fff8dc")
    CRIMSON = ("crimson", "#dc143c")
    DARK_BLUE = ("darkblue", "#00008b")
    DARK_CYAN = ("darkcyan", "#008b8b")
    DARK_GOLDEN_ROD = ("darkgoldenrod", "#b8860b")
    DARK_GRAY = ("darkgray", "#a9a9a9")
    DARK_GREEN = ("darkgreen", "#006400")
    DARK_KHAKI = ("darkkhaki", "#bdb76b")
    DARK_MAGENTA = ("darkmagenta", "#8b008b")
    DARK_OLIVE_GREEN = ("darkolivegreen", "#556b2f")
    DARK_ORANGE = ("darkorange", "#ff8c00")
    DARK_ORCHID = ("darkorchid", "#9932cc")
    DARK_RED = ("darkred", "#8b0000")
    DARK_SALMON = ("darksalmon", "#e9967a")
    DARK_SEA_GREEN = ("darkseagreen", "#8fbc8f")
    DARK_SLATE_BLUE = ("darkslateblue", "#483d8b")
    DARK_SLATE_GRAY = ("darkslategray", "#2f4f4f")
    DARK_TURQUOISE = ("darkturquoise", "#00ced1")
    DARK_VIOLET = ("darkviolet", "#9400d3")
    DEEP_PINK = ("deeppink", "#ff1493")
    DEEP_SKY_BLUE = ("deepskyblue", "#00bfff")
    DIM_GRAY = ("dimgray", "#696969")
    DODGER_BLUE = ("dodgerblue", "#1e90ff")
    FIRE_BRICK = ("firebrick", "#b22222")
    FLORALWHITE = ("floralwhite", "#fffaf0")
    FOREST_GREEN = ("forestgreen", "#228b22")
    FUCHSIA = ("fuchsia", "#ff00ff")
    GAINSBORO = ("gainsboro", "#dcdcdc")
    GHOSTWHITE = ("ghostwhite", "#f8f8ff")
    GOLD = ("gold", "#ffd700")
    GOLDEN_ROD = ("goldenrod", "#daa520")
    GRAY = ("gray", "#808080")
    GREEN = ("green", "#008000")
    GREEN_YELLOW = ("greenyellow", "#adff2f")
    HONEY_DEW = ("honeydew", "#f0fff0")
    HOT_PINK = ("hotpink", "#ff69b4")
    INDIAN_RED = ("indianred", "#cd5c5c")
    INDIGO = ("indigo", "#4b0082")
    IVORY = ("ivory", "#fffff0")
    KHAKI = ("khaki", "#f0e68c")
    LAVENDER = ("lavender", "#e6e6fa")
    LAVENDER_BLUSH = ("lavenderblush", "#fff0f5")
    LAWN_GREEN = ("lawngreen", "#7cfc00")
    LEMON_CHIFFON = ("lemonchiffon", "#fffacd")
    LIGHT_BLUE = ("lightblue", "#add8e6")
    LIGHT_CORAL = ("lightcoral", "#f08080")
    LIGHT_CYAN = ("lightcyan", "#e0ffff")
    LIGHT_GOLDEN_ROD_YELLOW = ("lightgoldenrodyellow", "#fafad2")
    LIGHT_GRAY = ("lightgray", "#d3d3d3")
    LIGHT_GREEN = ("lightgreen", "#90ee90")
    LIGHT_PINK = ("lightpink", "#ffb6c1")
    LIGHT_SALMON = ("lightsalmon", "#ffa07a")
    LIGHT_SEA_GREEN = ("lightseagreen", "#20b2aa")
    LIGHT_SKY_BLUE = ("lightskyblue", "#87cefa")
    LIGHT_SLATE_GRAY = ("lightslategray", "#778899")
    LIGHT_STEEL_BLUE = ("lightsteelblue", "#b0c4de")
    LIGHT_YELLOW = ("lightyellow", "#ffffe0")
    LIME = ("lime", "#00ff00")
    LIME_GREEN = ("limegreen", "#32cd32")
    LINEN = ("linen", "#faf0e6")
    MAROON = ("maroon", "#800000")
    MEDIUM_AQUA_MARINE = ("mediumaquamarine", "#66cdaa")
    MEDIUM_BLUE = ("mediumblue", "#0000cd")
    MEDIUM_ORCHID = ("mediumorchid", "#ba55d3")
    MEDIUM_PURPLE = ("mediumpurple", "#9370db")
    MEDIUM_SEA_GREEN = ("mediumseagreen", "#3cb371")
    MEDIUM_SLATE_BLUE = ("mediumslateblue", "#7b68ee")
    MEDIUM_SPRING_GREEN = ("mediumspringgreen", "#00fa9a")
    MEDIUM_TURQUOISE = ("mediumturquoise", "#48d1cc")
    MEDIUM_VIOLET_RED = ("mediumvioletred", "#c71585")
    MIDNIGHT_BLUE = ("midnightblue", "#191970")
    MINT_CREAM = ("mintcream", "#f5fffa")
    MISTY_ROSE = ("mistyrose", "#ffe4e1")
    MOCCASIN = ("moccasin", "#ffe4b5")
    NAVAJOWHITE = ("navajowhite", "#ffdead")
    NAVY = ("navy", "#000080")
    OLD_LACE = ("oldlace", "#fdf5e6")
    OLIVE = ("olive", "#808000")
    OLIVE_DRAB = ("olivedrab", "#6b8e23")
    ORANGE = ("orange", "#ffa500")
    ORANGE_RED = ("orangered", "#ff4500")
    ORCHID = ("orchid", "#da70d6")
    PALE_GOLDEN_ROD = ("palegoldenrod", "#eee8aa")
    PALE_GREEN = ("palegreen", "#98fb98")
    PALE_TURQUOISE = ("paleturquoise", "#afeeee")
    PALE_VIOLET_RED = ("palevioletred", "#db7093")
    PAPAYAWHIP = ("papayawhip", "#ffefd5")
    PEACH_PUFF = ("peachpuff", "#ffdab9")
    PERU = ("peru", "#cd853f")
    PINK = ("pink", "#ffc0cb")
    PLUM = ("plum", "#dda0dd")
    POWDER_BLUE = ("powderblue", "#b0e0e6")
    PURPLE = ("purple", "#800080")
    REBECCA_PURPLE = ("rebeccapurple", "#663399")
    RED = ("red", "#ff0000")
    ROSY_BROWN = ("rosybrown", "#bc8f8f")
    ROYAL_BLUE = ("royalblue", "#4169e1")
    SADDLE_BROWN = ("saddlebrown", "#8b4513")
    SALMON = ("salmon", "#fa8072")
    SANDY_BROWN = ("sandybrown", "#f4a460")
    SEA_GREEN = ("seagreen", "#2e8b57")
    SEA_SHELL = ("seashell", "#fff5ee")
    SIENNA = ("sienna", "#a0522d")
    SILVER = ("silver", "#c0c0c0")
    SKY_BLUE = ("skyblue", "#87ceeb")
    SLATE_BLUE = ("slateblue", "#6a5acd")
    SLATE_GRAY = ("slategray", "#708090")
    SNOW = ("snow", "#fffafa")
    SPRING_GREEN = ("springgreen", "#00ff7f")
    STEEL_BLUE = ("steelblue", "#4682b4")
    TAN = ("tan", "#d2b48c")
    TEAL = ("teal", "#008080")
    THISTLE = ("thistle", "#d8bfd8")
    TOMATO = ("tomato", "#ff6347")
    TURQUOISE = ("turquoise", "#40e0d0")
    VIOLET = ("violet", "#ee82ee")
    WHEAT = ("wheat", "#f5deb3")
    WHITE = ("white", "#ffffff")
    WHITE_SMOKE = ("whitesmoke", "#f5f5f5")
    YELLOW = ("yellow", "#ffff00")
    YELLOW_GREEN = ("yellowgreen", "#9acd32")

    @classmethod
    def get_by_color_name(cls, color_name):
        values = cls.list_values()
        for value in values:
            if color_name == value[0]:
                return cls(value) 
