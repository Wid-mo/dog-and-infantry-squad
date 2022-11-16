from manim import *


class DogAndInfantrySquad(Scene):
    def construct(self):
        """INTRODUCTION"""

        infantry_squad = Square(
            side_length=3, color=GREEN, fill_opacity=0.3, stroke_color=GREEN
        )
        infantry_squad.shift(0.5 * infantry_squad.side_length * DOWN)
        INFANTRY_SQUAD_TOTAL_SHIFT = infantry_squad.side_length * UP
        dog = Dot().next_to(infantry_squad, DOWN, buff=0)
        DOG_POS_FIRST_PHASE = UP
        numberPlane = NumberPlane()

        TOTAL_ANIMATION_TIME = 2
        T_1 = (0.5 * (2**0.5)) * TOTAL_ANIMATION_TIME
        T_2 = TOTAL_ANIMATION_TIME - T_1
        INFANTRY_SQUAD_FIRST_SHIFT = (0.5 * (2**0.5)) * INFANTRY_SQUAD_TOTAL_SHIFT
        g = VGroup(infantry_squad, dog)
        self.add(numberPlane, g)
        self.wait()
        # anim first phase (count time and shift)
        # anim second phase (2 - count time and move to)

        # self.play(g.animate.shift(infantry_squad.side_length * UP))
        # self.wait()

        # self.add(numberPlane, infantry_squad, dog)
        # self.wait()
        # self.play(
        #     infantry_squad.animate(rate_func=linear, run_time=2).shift(
        #         infantry_squad.side_length * UP
        #     ),
        #     dog.animate(rate_func=linear, run_time=1.5).move_to(DOG_POS_FIRST_PHASE),
        # )
        # self.wait()


# manim -p -ql dog_and_infantry_squad.py DogAndInfantrySquad
