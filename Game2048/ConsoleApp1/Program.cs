using System;

namespace Program {
    class Program {
        private static Grid grid = new Grid(4, 4);
        static void Main() {
            StartGame();
        }

        public static void StartGame() {
            grid.RandomGrid();
            grid.PrintGrid();
            Console.WriteLine("Press the up, down, left or right arrows");

            while (grid.IsGameOver == false) {
                if (Play() == false) {
                    if (grid.IsGameOver) {
                        Console.WriteLine("Game Over");
                        break;
                    }
                    continue;
                }

                grid.RandomGrid();
                Console.Clear();
                grid.PrintGrid();
            }
        }

        public static bool Play() {
            bool isCanMove = false;
            while (true) {
                bool isRightKey = false;
                ConsoleKeyInfo info = Console.ReadKey();
                switch (info.Key) {
                    case ConsoleKey.UpArrow:
                        isRightKey = true;
                        isCanMove = grid.MoveDirection(Direction.Up);
                        if (isCanMove == false) {
                            Console.WriteLine("Can't move up!");
                        }
                        break;
                    case ConsoleKey.DownArrow:
                        isRightKey = true;
                        isCanMove = grid.MoveDirection(Direction.Dowm);
                        if (isCanMove == false) {
                            Console.WriteLine("Can't move down!");
                        }
                        break;
                    case ConsoleKey.LeftArrow:
                        isRightKey = true;
                        isCanMove = grid.MoveDirection(Direction.Left);
                        if (isCanMove == false) {
                            Console.WriteLine("Can't move left!");
                        }
                        break;
                    case ConsoleKey.RightArrow:
                        isRightKey = true;
                        isCanMove = grid.MoveDirection(Direction.Right);
                        if (isCanMove == false) {
                            Console.WriteLine("Can't move right!");
                        }
                        break;
                }
                if (isRightKey) {
                    break;
                }
            }
            return isCanMove;
        }
    }
}
