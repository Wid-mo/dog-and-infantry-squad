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
        self.next_section("Cues 3/3", skip_animations=True)

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
        one_next_text = one_text.copy().next_to(s1_b, LEFT, buff=0.3)
        t1_alone_next_text = MarkupText("t<sub>1</sub> + ").next_to(s1_b, LEFT, buff=1)
        self.play(
            Transform(squad_line_b, s1_b),
            Transform(squad_marker_b, s1_b),
            ReplacementTransform(one_text, one_next_text),
            ReplacementTransform(t1_alone_text, t1_alone_next_text),
        )
        self.wait()

        s1_text = MarkupText("s<sub>1</sub> = t<sub>1</sub> + 1").next_to(s1_b, LEFT)
        self.play(FadeOut(one_next_text, t1_alone_next_text), FadeIn(s1_text))
        self.wait()
        self.clear()

        """MATH"""
        self.next_section("Math")

        self.add(Text("MATH"))
        self.wait()
        self.clear()

        # fe = {"substrings_to_isolate": ["\over", "="]}
        # e = {"substrings_to_isolate": "+"}
        # fmt: off
        # equations
        # eq = VGroup(
        #     MathTex(r"V_1 = V_2", substrings_to_isolate=["V_1", "=", "V_2"]),
        #     MathTex(r"{s_1 \over t_1} = {s_2 \over t_2}", substrings_to_isolate=["{", "s_1", "\over", "t_1", "}", "=", "s_2", "t_2"]),
        #     MathTex(r"{s_1 \over t_1} = {s_1-1 \over t_2}", substrings_to_isolate=["{", "s_1", "\over", "t_1", "}", "=", "s_1-1", "t_2"]),
        #     MathTex(r"{s_1 \over t_1} = {s_1-1 \over 1-t_1}", substrings_to_isolate=["{", "s_1", "\over", "t_1", "}", "=", "s_1-1","1-t_1"]),
        #     MathTex(r"{t_1+1 \over t_1} = {t_1+1-1 \over 1-t_1}", substrings_to_isolate=["{", "t_1+1", "\over", "t_1", "}", "=", "+1-1", "1-t_1"]),
        #     MathTex(r"{t_1+1 \over t_1} = {t_1 \over 1-t_1}", substrings_to_isolate=["{", "t_1+1", "\over", "t_1", "}", "=", "1-t_1"]),
        #     MathTex(r"{t_1+1 \over t_1} = {t_1 \over 1-t_1}", substrings_to_isolate=["{", "t_1", "+1", "\over", "t_1", "}", "=", "1-", "t_1"]),
        #     MathTex(r"{t+1 \over t } = {t \over 1-t }", substrings_to_isolate=["{", "t", "+1", "\over", "t", "}", "=", "1-", "t"]),
        #     MathTex("{", "t+1", r"\over", "t", "}", "=", "{", "t", r"\over", "1-t", "}"),
        #     MathTex(r"t^2 = (t+1)(1-t)", substrings_to_isolate="="),
        #     MathTex(r"t^2 = -(t + 1)(t - 1)", substrings_to_isolate="="),
        #     MathTex(r"t^2 = -(t^2 - 1^2)", substrings_to_isolate="="),
        #     MathTex(r"t^2 = -t^2 + 1", substrings_to_isolate="="),
        #     MathTex(r"2t^2 = 1", substrings_to_isolate="="),
        #     MathTex(r"t = \frac{\sqrt2}{2}", substrings_to_isolate="="),
        #     MathTex(r"t_1 \approx 71\%"),
        #     MathTex(r"s_1 + s_2 = ?", substrings_to_isolate=["+", "="]),
        #     MathTex(r"(t_1 + 1) + (s_1 - 1)", substrings_to_isolate="+"),
        #     MathTex(r"(t_1 + 1) + (t_1 + 1 - 1)", substrings_to_isolate="+"),
        #     MathTex(r"(\frac{\sqrt2}{2} + 1) + (\frac{\sqrt2}{2})", **e),
        # ).scale(2)
        # fmt: on

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

        # replacemect



        self.play(FadeOut(nx))

        # fmt: on

        # i = 0
        # self.play(*[Write(e) for e in eq[i]])  # V_1 = V_2
        # self.wait()
        # self.play(TransformMatchingTex(eq[i], eq[i+1], key_map={"V_1": "s_1", "V_2": "s_2"})); i += 1
        # self.wait()
        # self.play(ReplacementTransform(eq[i], eq[i+1])); i += 1
        # self.wait()
        # self.play(ReplacementTransform(eq[i], eq[i+1])); i += 1
        # self.wait()
        # self.play(ReplacementTransform(eq[i], eq[i+1])); i += 1
        # self.wait()
        # self.play(ReplacementTransform(eq[i], eq[i+1])); i += 1

        # eq[6].replace(eq[5])
        # self.play(
        #     TransformMatchingTex(
        #         eq[6], eq[7], path_arc=90 * DEGREES, transform_mismatches=True
        #     )
        # )
        # self.wait()

        # transitions_data: tuple[str, dict | None] = (
        #     ("TransformMatchingTex", {"V_1": "s_1", "V_2": "s_2"}),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None), # TransformMatchingTex(tex1, tex2, path_arc=90 * DEGREES, transform_mismatches=True)
        #     ("ReplacementTransform", None), # TransformMatchingTex(tex1, tex2, path_arc=90 * DEGREES, key_map={"t": "t^2"})
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        #     ("ReplacementTransform", None),
        # )
        # transitions = (
        #     createAnim(name, eq[i], eq[i + 1], key_map)
        #     for i, (name, key_map) in enumerate(transitions_data)
        # )

        # def createAnim(
        #     anim: str, src: Mobject, dest: Mobject, key_map: dict
        # ) -> Animation:
        #     return (
        #         TransformMatchingTex(src, dest, key_map=key_map)
        #         if anim == "TransformMatchingTex"
        #         else ReplacementTransform(src, dest)
        #     )

        # self.play(*[Write(e) for e in eq[0]])
        # self.wait()

        # for transition in transitions:
        #     self.play(transition)
        #     self.wait()

        # tex1, tex2 = MathTex(r"{s_1 \over t_1} = {s_1-1 \over t_2}", substrings_to_isolate=["{", "s_1", "\over", "t_1", "}", "=", "s_1-1", "t_2"]), MathTex(r"{s_1 \over t_1} = {s_1-1 \over 1-t_1}", substrings_to_isolate=["{", "s_1", "\over", "t_1", "}", "=", "s_1-1","1-t_1"])
        # self.add(tex1)
        # self.wait()
        # self.play(TransformMatchingTex(tex1, tex2, path_arc=90* DEGREES))
        # self.wait()

        # tex1 = MathTex(r"{t_1+1 \over t_1 } = {t_1 \over 1-t_1 }", substrings_to_isolate=["{", "t_1", "+1", "\over", "t_1", "}", "=", "1-", "t_1"])
        # tex2 = MathTex(r"{t+1 \over t } = {t \over 1-t }", substrings_to_isolate=["{", "t", "+1", "\over", "t", "}", "=", "1-", "t"])
        # self.add(tex1)
        # self.play(
        #     TransformMatchingTex(
        #         tex1, tex2, path_arc=90 * DEGREES, transform_mismatches=True
        #     )
        # )

        # tex1 = MathTex(
        #     "{", "t+1", r"\over", "t", "}", "=", "{", "t", r"\over", "1-t", "}"
        # )
        # self.play(LaggedStart(*[FadeIn(t) for t in tex1], lag_ratio=0.9), run_time=6)
        # tex2 = MathTex(r"t^2", "=", "(", "t+1", ")", "(", "1-t", ")")
        # self.play(
        #     TransformMatchingTex(
        #         tex1, tex2, path_arc=90 * DEGREES, key_map={"t": "t^2"}
        #     )
        # )

        # lines_to_up = lines[-1].copy().shift(UP)
        # self.play(ReplacementTransform(lines[-1], lines_to_up))
        # b1 = Brace(lines[-1][0], direction=DOWN, buff=1)
        # b1_text = MathTex(r"\approx 1.71").next_to(b1, DOWN)
        # b2 = Brace(lines[-1][2], direction=DOWN, buff=1)
        # b2_text = MathTex(r"\approx 0.71").next_to(b2, DOWN)
        # self.play(FadeIn(b1, b2, b1_text, b2_text))
        # self.wait()
        # self.remove(lines_to_up)

        # sol = MathTex(r"\sqrt2 + 1").scale(2).shift(UP)
        # sol_b = Brace(sol, direction=DOWN, buff=1)
        # sol_b_text = MathTex(r"\approx 2.42").scale(2).next_to(sol_b, DOWN)
        # self.play(
        #     ReplacementTransform(lines[-1], sol),
        #     ReplacementTransform(Group(b1, b2), sol_b),
        #     ReplacementTransform(Group(b1_text, b2_text), sol_b_text),
        # )
        # self.wait()

        """SOLUTION"""
        self.next_section("Solution", skip_animations=True)

        infantry_squad.shift(INFANTRY_SQUAD_SECOND_SHIFT)
        dog.shift(INFANTRY_SQUAD_TOTAL_SHIFT)
        s1_text = Text("1.71").next_to(s1_b, LEFT)
        s2_line = Line(ORIGIN, DOG_POS_FIRST_PHASE)
        s2_b = Brace(s2_line, direction=RIGHT, buff=2)
        s2_text = Text("0.71").next_to(s2_b, RIGHT)
        g.remove(question_text)
        self.add(SQUAD_MARKER, infantry_squad, s1_b, s2_b, s1_text, s2_text, g)
        self.wait()

        answer_text = Text("DISTANCE = 2.42").scale(2).set_color(RED).shift(1.5 * DOWN)
        self.play(FadeIn(answer_text))
        self.wait()


# manim -p -ql dog_and_infantry_squad.py DogAndInfantrySquad
