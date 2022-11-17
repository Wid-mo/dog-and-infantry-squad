from manim import *


class DogAndInfantrySquad(Scene):
    def construct(self):
        """INTRODUCTION"""

        infantry_squad = Square(
            side_length=3, color=GREEN, fill_opacity=0.3, stroke_color=GREEN
        )
        INFANTRY_SQUAD_TOTAL_SHIFT = infantry_squad.side_length * UP
        infantry_squad.shift(0.5 * -INFANTRY_SQUAD_TOTAL_SHIFT)
        dog = Dot(infantry_squad.get_bottom()).scale(3).set_color(RED)
        SQUAD_MARKER = (
            Group(
                DashedLine(DOWN + LEFT, DOWN + RIGHT),
                DashedLine(DOWN + RIGHT, UP + RIGHT),
                DashedLine(UP + RIGHT, UP + LEFT),
                DashedLine(UP + LEFT, DOWN + LEFT),
            )
            .scale(1.5)
            .shift(0.5 * -INFANTRY_SQUAD_TOTAL_SHIFT)
        )
        self.play(FadeIn(SQUAD_MARKER, infantry_squad, dog))

        two_phases_animation_time = 3
        SQRT2_OVER_2 = 0.5 * (2**0.5)
        T_1 = SQRT2_OVER_2 * two_phases_animation_time
        INFANTRY_SQUAD_FIRST_SHIFT = SQRT2_OVER_2 * INFANTRY_SQUAD_TOTAL_SHIFT
        self.play(
            infantry_squad.animate.shift(INFANTRY_SQUAD_FIRST_SHIFT),
            dog.animate.shift(INFANTRY_SQUAD_FIRST_SHIFT + INFANTRY_SQUAD_TOTAL_SHIFT),
            run_time=T_1,
            rate_func=linear,
        )

        T_2 = two_phases_animation_time - T_1
        INFANTRY_SQUAD_SECOND_SHIFT = (
            INFANTRY_SQUAD_TOTAL_SHIFT - INFANTRY_SQUAD_FIRST_SHIFT
        )
        self.play(
            infantry_squad.animate.shift(INFANTRY_SQUAD_SECOND_SHIFT),
            dog.animate.shift(INFANTRY_SQUAD_SECOND_SHIFT - INFANTRY_SQUAD_TOTAL_SHIFT),
            run_time=T_2,
            rate_func=linear,
        )
        self.wait()

        # show arrow and text label

        question_text = Text("DISTANCE = ?").scale(7).set_color(RED)
        g = VGroup(question_text)
        self.play(FadeOut(dog), FadeIn(g))


# manim -p -ql dog_and_infantry_squad.py DogAndInfantrySquad
