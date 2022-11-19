from manim import *


class DogAndInfantrySquad(Scene):
    def construct(self):
        """INTRODUCTION"""
        self.next_section("Introduction", skip_animations=True)

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

        question_text = Text("DISTANCE = ?").scale(2).set_color(RED).shift(RIGHT + DOWN)
        line1 = Line(
            -INFANTRY_SQUAD_TOTAL_SHIFT + 0.1 * LEFT,
            INFANTRY_SQUAD_TOTAL_SHIFT + 0.1 * LEFT,
        )
        line2 = Line(
            INFANTRY_SQUAD_TOTAL_SHIFT + 0.1 * LEFT,
            INFANTRY_SQUAD_TOTAL_SHIFT + 0.1 * RIGHT,
        )
        arrow = Arrow(INFANTRY_SQUAD_TOTAL_SHIFT + 0.1 * RIGHT, 0.1 * RIGHT, buff=0)
        g = VGroup(question_text, line1, line2, arrow).set_color(RED)
        self.play(FadeOut(dog), FadeIn(g))
        self.wait()
        self.clear()

        """CUES 1/3"""
        self.next_section("Cues 1 / 3", skip_animations=True)

        self.add(Text("PAUSE"), Text("and try to solve").shift(DOWN))
        self.wait(duration=3)
        self.clear()
        self.add(Text("CUES 1 / 3"))
        self.wait(duration=1)
        self.clear()
        self.add(MarkupText("SIMPLIFY    s<sub>2</sub>"))
        self.wait(duration=1)
        self.clear()

        DOG_POS_FIRST_PHASE = INFANTRY_SQUAD_FIRST_SHIFT
        s1_line = Line(
            -INFANTRY_SQUAD_TOTAL_SHIFT,
            DOG_POS_FIRST_PHASE,
        ).set_color(RED)
        dog.move_to(DOG_POS_FIRST_PHASE)
        infantry_squad.shift(-INFANTRY_SQUAD_SECOND_SHIFT)
        s2_line = Line(DOG_POS_FIRST_PHASE, ORIGIN)
        s2_b = Brace(
            s2_line,
            direction=s2_line.copy().rotate(-PI / 2).get_unit_vector(),
            buff=2,
        )
        s2_text = MarkupText("s<sub>2</sub>").next_to(s2_b, RIGHT)
        self.add(SQUAD_MARKER, infantry_squad, s1_line, dog, s2_b, s2_text)
        self.wait()

        s1_b = Brace(
            s1_line,
            direction=s1_line.copy().rotate(PI / 2).get_unit_vector(),
            buff=2,
        ).set_color(RED)
        s1_text = MarkupText("s<sub>1</sub>").next_to(s1_b, LEFT).set_color(RED)
        side_text = Text("1").next_to(SQUAD_MARKER.get_left(), RIGHT)
        self.play(FadeIn(s1_b, s1_text, side_text))
        self.wait()

        squad_dashed_line = SQUAD_MARKER[-1].copy()  # left side
        squad_line = Line(-INFANTRY_SQUAD_TOTAL_SHIFT, ORIGIN)
        s2_text_next = MarkupText("s<sub>1</sub> - 1").next_to(s2_b, RIGHT)
        side_text_next = Text("1").next_to(squad_line, RIGHT)
        self.play(
            Transform(squad_dashed_line, squad_line),
            Transform(side_text, side_text_next),
        )
        self.wait()
        self.play(Transform(s2_text, s2_text_next))
        self.wait()
        self.clear()

        """CUES 2/3"""
        self.next_section("Cues 2/3", skip_animations=True)

        self.add(Text("CUES 2 / 3"))
        self.wait(duration=1)
        self.clear()
        self.add(MarkupText("TIME IN PERCENT UNITS"))
        self.wait(duration=1)
        self.clear()

        t1_b = Brace(
            s1_line,
            direction=s1_line.copy().rotate(PI / 2).get_unit_vector(),
            buff=2,
        )
        t1_text = MarkupText("t<sub>1</sub>").next_to(t1_b, LEFT)
        t2_b = Brace(
            s2_line,
            direction=s2_line.copy().rotate(PI / 2).get_unit_vector(),
            buff=2,
        )
        t2_text = MarkupText("t<sub>2</sub>").next_to(t2_b, RIGHT)
        self.add(SQUAD_MARKER, infantry_squad, t1_b, t1_text, t2_b, t2_text)
        self.wait()

        self.play(FadeIn(MarkupText("t<sub>1</sub> + t<sub>2</sub> = 1").to_edge(UP)))
        self.wait()

        t2_text_next = MarkupText("1 - t<sub>1</sub>").next_to(t2_b, RIGHT)
        self.play(Transform(t2_text, t2_text_next))
        self.wait()
        self.clear()

        """CUES 3/3"""
        self.next_section("Cues 3/3")

        self.add(Text("CUES 3 / 3"))
        self.wait(duration=1)
        self.clear()
        self.add(MarkupText("SIMPLITY s<sub>1</sub>"))
        self.wait(duration=1)
        self.clear()

        infantry_squad.shift(INFANTRY_SQUAD_SECOND_SHIFT)
        dog.move_to(ORIGIN)
        all_height_line = Line(-INFANTRY_SQUAD_TOTAL_SHIFT, INFANTRY_SQUAD_TOTAL_SHIFT)
        all_height_text = Text("2").next_to(all_height_line, RIGHT)
        self.add(SQUAD_MARKER, infantry_squad, all_height_line, all_height_text)
        self.wait()

        squad_line = Line(
            infantry_squad.get_bottom(), infantry_squad.get_top()
        ).set_color(RED)
        squad_text = Text("1").next_to(squad_line, RIGHT).set_color(RED)
        self.play(FadeIn(squad_line, squad_text))
        self.wait()

        total_distance_line = Line(
            all_height_line, end=all_height_line.get_end() - INFANTRY_SQUAD_TOTAL_SHIFT
        )
        # TODO remove distance line and add new with half length
        total_distance_text = Text("1").next_to(total_distance_line, RIGHT)
        self.play(
            ReplacementTransform(all_height_line, total_distance_line),
            ReplacementTransform(all_height_text, total_distance_text),
            FadeOut(squad_line, squad_text),
        )
        self.wait()

        squad_marker_b = Brace(total_distance_line, direction=LEFT, buff=2)
        t1_plus_t2_text = MarkupText("1*(t<sub>1</sub> + t<sub>2</sub>)").next_to(
            squad_marker_b, LEFT
        )
        self.play(
            FadeIn(squad_marker_b),
            ReplacementTransform(total_distance_text, t1_plus_t2_text),
            FadeOut(total_distance_line),
        )
        self.wait()

        INFANTRY_SQUAD_FIRST_PHASE = infantry_squad.copy().shift(
            -INFANTRY_SQUAD_SECOND_SHIFT
        )
        line = Line(-INFANTRY_SQUAD_TOTAL_SHIFT, -INFANTRY_SQUAD_TOTAL_SHIFT)
        dog.move_to(-INFANTRY_SQUAD_TOTAL_SHIFT)
        dog_dest = dog.copy().move_to(DOG_POS_FIRST_PHASE)
        line_for_brace = Line(
            -INFANTRY_SQUAD_TOTAL_SHIFT,
            -INFANTRY_SQUAD_TOTAL_SHIFT + INFANTRY_SQUAD_FIRST_SHIFT,
        )
        squad_marker_next_b = Brace(line_for_brace, direction=LEFT, buff=2)
        # TODO divide text and proper translate it
        text_with_t1_text = MarkupText("1*(t<sub>1</sub>          )").next_to(
            squad_marker_next_b, LEFT
        )
        self.play(
            Transform(infantry_squad, INFANTRY_SQUAD_FIRST_PHASE),
            Transform(line, s1_line.set_color(WHITE)),
            Transform(dog, dog_dest),
            Transform(squad_marker_b, squad_marker_next_b),
            ReplacementTransform(t1_plus_t2_text, text_with_t1_text),
            run_time=2,
        )
        self.wait()


# manim -p -ql dog_and_infantry_squad.py DogAndInfantrySquad
