from manim import *


class DogAndInfantrySquad(Scene):
    def construct(self):
        """INTRODUCTION"""
        self.next_section("Introduction", skip_animations=False)

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

        DOG_POS_FIRST_PHASE = INFANTRY_SQUAD_FIRST_SHIFT
        question_text = Text("DISTANCE = ?").scale(2).set_color(RED).shift(RIGHT + DOWN)
        line1 = Line(
            -INFANTRY_SQUAD_TOTAL_SHIFT + 0.1 * LEFT,
            DOG_POS_FIRST_PHASE + 0.1 * LEFT,
        )
        line2 = Line(
            DOG_POS_FIRST_PHASE + 0.1 * LEFT,
            DOG_POS_FIRST_PHASE + 0.1 * RIGHT,
        )
        arrow = Arrow(DOG_POS_FIRST_PHASE + 0.1 * RIGHT, 0.1 * RIGHT, buff=0)
        g = VGroup(question_text, line1, line2, arrow).set_color(RED)
        self.play(FadeOut(dog), FadeIn(g))
        self.wait()
        self.clear()

        """CUES 1/3"""
        self.next_section("Cues 1 / 3", skip_animations=False)

        self.add(Text("PAUSE"), Text("and try to solve").shift(DOWN))
        self.wait(duration=2)
        self.clear()
        self.add(Text("CUES 1 / 3"))
        self.wait(duration=1)
        self.clear()
        self.add(MarkupText("SIMPLIFY    s<sub>2</sub>"))
        self.wait(duration=1)
        self.clear()

        s1_line = Line(
            -INFANTRY_SQUAD_TOTAL_SHIFT,
            DOG_POS_FIRST_PHASE,
        ).set_color(RED)
        dog.move_to(DOG_POS_FIRST_PHASE)
        infantry_squad.shift(-INFANTRY_SQUAD_SECOND_SHIFT)
        s2_line = Line(DOG_POS_FIRST_PHASE, ORIGIN)
        s2_b = Brace(s2_line, direction=RIGHT, buff=2)
        s2_text = MarkupText("s<sub>2</sub>").next_to(s2_b, RIGHT)
        self.add(SQUAD_MARKER, infantry_squad, s1_line, dog, s2_b, s2_text)
        self.wait()

        s1_b = Brace(
            s1_line,
            direction=s1_line.copy().rotate(PI / 2).get_unit_vector(),
            buff=2,
        ).set_color(RED)
        s1_text = MarkupText("s<sub>1</sub>").next_to(s1_b, LEFT).set_color(RED)
        self.play(FadeIn(s1_b, s1_text))
        self.wait()

        side_text = Text("1").next_to(SQUAD_MARKER.get_right(), RIGHT)
        self.play(FadeIn(side_text))
        squad_dashed_line = SQUAD_MARKER[1].copy()  # right side
        squad_line = Line(-INFANTRY_SQUAD_TOTAL_SHIFT, ORIGIN)
        side_next_text = Text("1").next_to(squad_line, RIGHT)
        self.play(
            Transform(squad_dashed_line, squad_line),
            ReplacementTransform(side_text, side_next_text),
        )
        self.wait()

        equals_text = Text(" = ").next_to(s2_text, RIGHT)
        s1_next_text = s1_text.copy().next_to(equals_text, RIGHT)
        plus_text = Text(" + ").next_to(s1_next_text, RIGHT)
        side_next_text2 = side_next_text.copy().next_to(plus_text, RIGHT)
        self.play(
            FadeIn(equals_text, plus_text),
            TransformFromCopy(s1_text, s1_next_text),
            TransformFromCopy(side_next_text, side_next_text2),
        )
        self.wait()
        self.clear()

        """CUES 2/3"""
        self.next_section("Cues 2/3", skip_animations=False)

        self.add(Text("CUES 2 / 3"))
        self.wait(duration=1)
        self.clear()
        self.add(Text("Entire travel"), Text("takes 1 unit of time").shift(DOWN))
        self.wait(duration=2)
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

        up_equation_text = MarkupText("t<sub>1</sub> + t<sub>2</sub> = 1").to_edge(UP)
        self.play(FadeIn(up_equation_text))
        self.wait()

        equals_one_text = up_equation_text[-2:].copy()
        equals_one_dest_text = equals_one_text.copy().next_to(t2_text, RIGHT)
        minus_text = Text("-").next_to(equals_one_dest_text, RIGHT)
        t1_text = up_equation_text[0:2].copy()
        t1_dest_text = t1_text.copy().next_to(minus_text, RIGHT)
        self.play(
            Transform(equals_one_text, equals_one_dest_text),
            FadeIn(minus_text),
            Transform(t1_text, t1_dest_text),
        )
        self.wait()
        self.clear()

        """CUES 3/3"""
        self.next_section("Cues 3/3", skip_animations=False)

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
        s1_b.set_color(WHITE)
        s1_text = MarkupText("s<sub>1</sub>").next_to(s1_b, LEFT)
        self.add(
            SQUAD_MARKER,
            infantry_squad,
            all_height_line,
            all_height_text,
            s1_b,
            s1_text,
        )
        self.wait()

        self.play(FadeOut(s1_b, s1_text))

        squad_line = Line(
            infantry_squad.get_bottom(), infantry_squad.get_top()
        ).set_color(RED)
        one_text = Text("1").next_to(squad_line, RIGHT).set_color(RED)
        self.play(FadeIn(squad_line, one_text))
        self.wait()

        total_distance_line = Line(
            all_height_line, end=all_height_line.get_end() - INFANTRY_SQUAD_TOTAL_SHIFT
        )
        self.remove(all_height_line)
        self.add(total_distance_line)
        total_distance_text = Text("1").next_to(total_distance_line, RIGHT)
        self.play(
            ReplacementTransform(all_height_text, total_distance_text),
            FadeOut(squad_line, one_text),
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
        dog.move_to(-INFANTRY_SQUAD_TOTAL_SHIFT)
        line_for_brace = Line(
            -INFANTRY_SQUAD_TOTAL_SHIFT,
            -INFANTRY_SQUAD_TOTAL_SHIFT + INFANTRY_SQUAD_FIRST_SHIFT,
        )
        squad_marker_next_b = Brace(line_for_brace, direction=LEFT, buff=2)
        text_with_t1_text = MarkupText("1*t<sub>1</sub>").next_to(
            squad_marker_next_b, LEFT
        )
        self.play(
            Transform(infantry_squad, INFANTRY_SQUAD_FIRST_PHASE),
            Transform(squad_marker_b, squad_marker_next_b),
            ReplacementTransform(t1_plus_t2_text, text_with_t1_text),
            run_time=2,
        )
        self.wait()

        squad_line = Line(infantry_squad.get_bottom(), infantry_squad.get_top())
        squad_line_b = Brace(squad_line, direction=LEFT, buff=2).set_color(GREEN)
        one_text = Text("1").next_to(squad_line_b, LEFT).set_color(GREEN)
        t1_alone_text = MarkupText("t<sub>1</sub>").next_to(squad_marker_next_b, LEFT)
        self.play(
            FadeIn(squad_line_b, one_text),
            ReplacementTransform(text_with_t1_text, t1_alone_text),
        )
        self.wait()

        s1_b.set_color(WHITE)
        one_next_text = one_text.copy().next_to(s1_b, LEFT)
        t1_alone_next_text = MarkupText("t<sub>1</sub> + ").next_to(one_next_text, LEFT)
        self.play(
            Transform(squad_line_b, s1_b),
            Transform(squad_marker_b, s1_b),
            ReplacementTransform(one_text, one_next_text),
            ReplacementTransform(t1_alone_text, t1_alone_next_text),
        )
        self.wait()

        s1_text = MarkupText("s<sub>1</sub> =").next_to(t1_alone_next_text, LEFT)
        self.play(
            FadeIn(s1_text), one_next_text.animate.next_to(t1_alone_next_text, RIGHT)
        )
        self.wait()
        self.clear()

        """MATH"""
        self.next_section("Math", skip_animations=False)

        self.add(Text("MATH"))
        self.wait()
        self.clear()

        # fmt: off

        self.play(Write(MathTex("V_1 = V_2").scale(2)))
        self.wait()
        self.clear()

        pr = MathTex(r"V_1 = V_2", substrings_to_isolate=["V_1", "=", "V_2"]).scale(2)
        nx = MathTex(
            r"{s_1 \over t_1} = {s_2 \over t_2}",
            substrings_to_isolate=["{", "s_1", "\over", "t_1", "}", "=", "s_2", "t_2"],
        )
        nx.scale(2)
        self.play(TransformMatchingTex(pr, nx, key_map={"V_1": "s_1", "V_2": "s_2"}))
        self.wait()

        pr = nx
        nx = MathTex(r"{s_1 \over t_1} = {s_1-1 \over t_2}", substrings_to_isolate=["{", "s_1", "\over", "t_1", "}", "=", "s_1-1", "t_2"])
        nx.scale(2)
        self.play(ReplacementTransform(pr, nx))
        self.wait()

        pr = nx
        nx = MathTex(r"{s_1 \over t_1} = {s_1-1 \over 1-t_1}", substrings_to_isolate=["{", "s_1", "\over", "t_1", "}", "=", "s_1-1","1-t_1"])
        nx.scale(2)
        self.play(ReplacementTransform(pr, nx))
        self.wait()

        pr = nx
        nx = MathTex(r"{t_1+1 \over t_1} = {t_1+1-1 \over 1-t_1}", substrings_to_isolate=["{", "t_1+1", "\over", "t_1", "}", "=", "+1-1", "1-t_1"])
        nx.scale(2)
        self.play(ReplacementTransform(pr, nx))
        self.wait()

        pr = nx
        nx = MathTex(r"{t_1+1 \over t_1} = {t_1 \over 1-t_1}", substrings_to_isolate=["{", "t_1+1", "\over", "t_1", "}", "=", "1-t_1"])
        nx.scale(2)
        self.play(ReplacementTransform(pr, nx))
        self.wait()
        self.remove(nx)

        pr = MathTex(r"{t_1+1 \over t_1 } = {t_1 \over 1-t_1 }", substrings_to_isolate=["{", "t_1", "+1", "\over", "t_1", "}", "=", "1-", "t_1"])
        pr.scale(2)
        nx = MathTex(r"{t+1 \over t } = {t \over 1-t }", substrings_to_isolate=["{", "t", "+1", "\over", "t", "}", "=", "1-", "t"])
        nx.scale(2)
        self.play(TransformMatchingTex(pr, nx, path_arc=90 * DEGREES, transform_mismatches=True))
        self.wait()
        self.remove(nx)

        pr = MathTex(r"{t+1 \over t} = {t \over 1-t}", substrings_to_isolate=["{", "t+1", "\over", "t", "}", "=", "1-t"])
        pr.scale(2)
        nx = MathTex(r"t^2 = (t+1)(1-t)", substrings_to_isolate=["t^2", "=", "(", "t+1", ")", "1-t"])
        nx.scale(2)
        self.play(TransformMatchingTex(pr, nx, path_arc=90 * DEGREES, key_map={"t": "t^2"}))
        self.wait()
        self.remove(nx)

        pr = MathTex(r"t^2 = (t+1)(1-t)", substrings_to_isolate=["t^2", "=", "(t+1)", "(", "1", "-", "t", ")"])
        pr.scale(2)
        nx = MathTex(r"t^2 = -(t+1)(t-1)", substrings_to_isolate=["t^2", "=", "-", "(t+1)", "t", "1"])
        nx.scale(2)
        self.play(TransformMatchingTex(pr, nx, path_arc=90 * DEGREES))
        self.wait()
        self.remove(nx)

        pr = MathTex(r"t^2 = -(t+1)(t-1)", substrings_to_isolate=["t^2 = ", "-", "t", "1"])
        pr.scale(2)
        nx = MathTex(r"t^2 = -(t^2 - 1^2)", substrings_to_isolate=["t^2 = ", "-", "t^2", "1^2", "(", ")"])
        nx.scale(2)
        self.play(TransformMatchingTex(pr, nx, path_arc=90 * DEGREES, key_map={"t": "t^2", "1": "1^2"}))
        self.wait()

        pr = nx
        nx = MathTex(r"t^2 = -t^2 + 1", substrings_to_isolate=["t^2 = ", "-", "t^2", "+", "1"])
        nx.scale(2)
        self.play(TransformMatchingTex(pr, nx, path_arc=90 * DEGREES, key_map={"1^2": "1"}))
        self.wait()

        pr = nx
        nx = MathTex(r"2t^2 = 1", substrings_to_isolate=["2t^2", "=", "1"])
        nx.scale(2)
        self.play(ReplacementTransform(pr, nx))
        self.wait()
        self.remove(nx)

        pr = MathTex(r"2t^2 = 1", substrings_to_isolate=["2", "t", "^2", "=", "1"]).scale(2)
        nx = MathTex(r"{{t}} = {\sqrt2 \over {{2}}}", substrings_to_isolate=["=", "{", "}", "\sqrt2"]) # I can't add 't' to isolate because \sqrt
        nx.scale(2)
        self.play(TransformMatchingTex(pr, nx, path_arc=90 * DEGREES, key_map={"^2": "\sqrt2"}))
        self.wait()
        self.remove(nx)

        pr = nx
        nx = MathTex(r"{{t}}_1 \approx 71\%").scale(2)
        self.play(ReplacementTransform(pr, nx))
        self.wait()

        self.play(FadeOut(nx))
        pr = MathTex(r"s_1 + s_2 {{= ?}}").scale(2)
        self.play(Write(pr))
        self.wait()

        nx = MathTex(r"s_1 + s_2").scale(2)
        self.play(ReplacementTransform(pr, nx))
        self.wait(0.5)
        self.remove(nx)

        pr = MathTex(r"s_1 + s_2", substrings_to_isolate=["s_1", "s_2"]).scale(2)
        nx = MathTex(r"(t_1 + 1) + (s_1 - 1)", substrings_to_isolate=["(t_1 + 1)", "(s_1 - 1)"]).scale(2)
        self.play(ReplacementTransform(pr, nx))
        self.wait()
        self.remove(nx)

        pr = MathTex(r"(t_1 + 1) + ({{s_1}} - 1)").scale(2)
        nx = MathTex(r"(t_1 + 1) + ({{t_1 + 1}} - 1)").scale(2)
        self.play(ReplacementTransform(pr, nx))
        self.wait()
        self.remove(nx)

        pr = MathTex(r"(t_1 + 1) + ({{t_1 + 1 - 1}})").scale(2)
        nx = MathTex(r"(t_1 + 1) + ({{t_1}})").scale(2)
        self.play(ReplacementTransform(pr, nx))
        self.wait()
        self.remove(nx)

        pr = MathTex(r"({{t_1}} + 1) + ({{t_1}})").scale(2)
        nx = MathTex(r"({{\frac{\sqrt2}{2}}} + 1) + ({{\frac{\sqrt2}{2}}})")
        nx.scale(2)
        self.play(ReplacementTransform(pr, nx))
        self.wait()

        # fmt: on

        self.play(nx.animate.shift(UP))
        self.remove(nx)
        nx = MathTex(r"{{(\frac{\sqrt2}{2} + 1)}} + {{(\frac{\sqrt2}{2})}}")
        nx.scale(2).shift(UP)
        self.add(nx)
        b1 = Brace(nx[0], direction=DOWN, buff=MED_LARGE_BUFF)
        b1_text = MathTex(r"\approx 1.71").next_to(b1, DOWN)
        b2 = Brace(nx[2], direction=DOWN, buff=MED_LARGE_BUFF)
        b2_text = MathTex(r"\approx 0.71").next_to(b2, DOWN)
        self.play(FadeIn(b1, b2, b1_text, b2_text))
        self.wait()
        self.remove(nx)

        sol = MathTex(r"\sqrt2 + 1").scale(2).shift(UP)
        sol_b = Brace(sol, direction=DOWN, buff=MED_LARGE_BUFF)
        sol_b_text = MathTex(r"\approx 2.41")
        sol_b_text.scale(2).next_to(sol_b, DOWN, buff=MED_LARGE_BUFF).set_color(RED)
        self.play(
            ReplacementTransform(nx, sol),
            ReplacementTransform(Group(b1, b2), sol_b),
            ReplacementTransform(Group(b1_text, b2_text), sol_b_text),
        )
        self.wait()
        self.clear()

        """SOLUTION"""
        self.next_section("Solution", skip_animations=False)

        infantry_squad.shift(INFANTRY_SQUAD_SECOND_SHIFT)
        dog.shift(INFANTRY_SQUAD_TOTAL_SHIFT)
        s1_text = Text("1.71").next_to(s1_b, LEFT)
        s2_line = Line(ORIGIN, DOG_POS_FIRST_PHASE)
        s2_b = Brace(s2_line, direction=RIGHT, buff=2)
        s2_text = Text("0.71").next_to(s2_b, RIGHT)
        g.remove(question_text)
        self.add(SQUAD_MARKER, infantry_squad, s1_b, s2_b, s1_text, s2_text, g)
        self.wait()

        answer_text = Text("DISTANCE = 2.41").scale(2).set_color(RED).shift(1.5 * DOWN)
        self.play(FadeIn(answer_text))
        self.wait()
        self.clear()

        """FUN FACT"""
        self.next_section("Fun fact", skip_animations=False)

        self.add(
            Text("FUN FACT").shift(UP),
            Text("Red point is 2.41 times faster \n than green square").shift(DOWN),
        )
        self.wait(2)


# manim -p -ql dog_and_infantry_squad.py DogAndInfantrySquad
