textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3


def draw_text(surface, text, color, rect, font, align=textAlignCenter, aa=False, bkg=None):
    line_spacing = -2
    space_width, font_height = font.size(" ")[0], font.size("Tg")[1]

    list_of_words = text.split(" ")
    if bkg:
        image_list = [font.render(word, 1, color, bkg) for word in list_of_words]
        for image in image_list: image.set_colorkey(bkg)
    else:
        image_list = [font.render(word, aa, color) for word in list_of_words]

    max_len = rect[2]
    line_len_list = [0]
    line_list = [[]]
    for image in image_list:
        width = image.get_width()
        line_len = line_len_list[-1] + len(line_list[-1]) * space_width + width
        if len(line_list[-1]) == 0 or line_len <= max_len:
            line_len_list[-1] += width
            line_list[-1].append(image)
        else:
            line_len_list.append(width)
            line_list.append([image])

    line_bottom = rect[1]
    last_line = 0
    for line_len, lineImages in zip(line_len_list, line_list):
        line_left = rect[0]
        if align == textAlignRight:
            line_left += + rect[2] - line_len - space_width * (len(lineImages) - 1)
        elif align == textAlignCenter:
            line_left += (rect[2] - line_len - space_width * (len(lineImages) - 1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            space_width = (rect[2] - line_len) // (len(lineImages) - 1)
        if line_bottom + font_height > rect[1] + rect[3]:
            break
        last_line += 1
        for i, image in enumerate(lineImages):
            x, y = line_left + i * space_width, line_bottom
            surface.blit(image, (round(x), y))
            line_left += image.get_width()
        line_bottom += font_height + line_spacing

    if last_line < len(line_list):
        draw_words = sum([len(line_list[i]) for i in range(last_line)])
        remaining_text = ""
        for text in list_of_words[draw_words:]: remaining_text += text + " "
        return remaining_text
    return ""

# 测试

# import pygame
#
# pygame.init()
# font = pygame.font.SysFont('Algerian', 40)
#
# msg = "Simple function that will draw text and wrap it to fit the rect passed.  If there is any text that will not fit into the box, the remaining text will be returned."
# textRect = pygame.Rect(100, 100, 300, 300)
#
# window = pygame.display.set_mode((500, 500))
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     window.fill((255, 255, 255))
#     pygame.draw.rect(window, (221, 12, 0), textRect)
#     # drawTextRect = textRect.inflate(-10, -10)
#     draw_text(window, msg, (0, 0, 0), textRect, font, textAlignCenter, True)
#     pygame.display.flip()
