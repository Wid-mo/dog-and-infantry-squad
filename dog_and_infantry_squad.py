from manim import *

class DogAndInfantrySquad(Scene):
    def construct(self):
        infantry_squad = Square(side_length=3, color=GREEN, fill_opacity=0.3, stroke_color=GREEN).shift(1.5*DOWN)
        dog = Dot().next_to(infantry_squad, DOWN, buff=0)
        DOG_POS_FIRST_PHASE = UP
        numberPlane = NumberPlane()

        self.add(numberPlane, infantry_squad, dog)
        self.wait()
        self.play(infantry_squad.animate(rate_func=linear, run_time=2).shift(infantry_squad.side_length*UP),
            dog.animate(rate_func=linear, run_time=1.5).move_to(DOG_POS_FIRST_PHASE)
            )
        self.wait()