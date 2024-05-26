from random import randint as r
from RGBMatrixDriver import RGBMatrix, RGBMatrixArguments, prefilled_matrix_options


# Support all the defaults that RGBMatrixDriver includes
args = RGBMatrixArguments().parse_args()

# Fill out an RGBMatrixOptions instance with all the arguments
options = prefilled_matrix_options(args)

# Create a matrix and canvas
matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

# Push the pixels!
while True:
    # Simulate static -- Set R, G, B equal to each other at random
    for y in range(matrix.height):
        for x in range(matrix.width):
            canvas.SetPixel(x, y, *tuple([r(0, 255)] * 3))

    canvas = matrix.SwapOnVSync(canvas)
    canvas = matrix.SwapOnVSync(canvas)
