def test(self):

        snake = Snake(100, 100, 1, (51, 51))
        snake.move((0, 0))
        return snake.length,snake.positions[0],snake.score