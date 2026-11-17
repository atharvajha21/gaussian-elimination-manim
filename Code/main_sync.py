
from manim import *


class GaussianElimination(Scene):

    def construct(self):

        self.camera.background_color = "#0B1020"

        # Fixed screen layout
        def heading(text):
            obj = Text(
                text,
                color="#F4C96B",
                font_size=24,
                weight=BOLD
            )
            obj.scale_to_fit_width(9)
            obj.scale_to_fit_height(0.48)
            obj.move_to(UP * 3.15)
            return obj

        def explanation(text):
            obj = Text(
                text,
                color=GRAY_B,
                font_size=16
            )
            obj.scale_to_fit_width(9.2)
            obj.move_to(DOWN * 2.55)
            return obj

        def equation(tex, position=ORIGIN, scale=0.75):
            obj = MathTex(
                tex,
                substrings_to_isolate=[
                    r"\boxed{1}",
                    r"\boxed{-1}",
                    r"\boxed{7}"
                ]
            )

            for pivot in [r"\boxed{1}", r"\boxed{-1}", r"\boxed{7}"]:
                obj.set_color_by_tex(pivot, "#F4C96B")
            obj.scale(scale)
            obj.scale_to_fit_width(7.8)
            obj.scale_to_fit_height(0.95)
            obj.move_to(position)
            return obj

        def show_step(title, tex, note, pause=4):
            h = heading(title)
            eq = equation(tex, UP * 0.25)
            note_obj = explanation(note)

            # Reveal each element with short, smooth transitions.
            self.play(FadeIn(h, shift=DOWN * 0.12), run_time=0.25)
            self.play(Write(eq), run_time=0.50)
            self.play(FadeIn(note_obj, shift=UP * 0.12), run_time=0.25)
            self.wait(pause)
            self.play(
                FadeOut(h),
                FadeOut(eq),
                FadeOut(note_obj),
                run_time=0.25
            )

        # 1. INTRODUCTION
        # ----------------------------------

        title = Text(
            "GAUSSIAN ELIMINATION",
            color="#F4C96B",
            font_size=42,
            weight=BOLD
        )

        subtitle = Text(
            "A Step-by-Step Visual Guide",
            color=WHITE,
            font_size=25
        ).next_to(title, DOWN, buff=0.5)

        student_details = VGroup(
            Text("ATHARVA JHA", color=YELLOW, font_size=21, weight=BOLD),
            Text("URN: E25B070903", color=WHITE, font_size=17),
            Text("Batch: Ramanujan", color=WHITE, font_size=17)
        ).arrange(DOWN, buff=0.16)

        student_details.next_to(subtitle, DOWN, buff=0.55)

        self.play(Write(title))
        self.wait(1)
        self.play(FadeIn(subtitle))
        self.play(FadeIn(student_details, shift=UP * 0.15))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(student_details))

        # ----------------------------------
        # 2. INTRODUCE THE EQUATIONS
        # ----------------------------------

        h = heading("Our System of Equations")

        eq1 = MathTex("x+y+z=6").scale(1.15)
        eq2 = MathTex("2x+y-z=1").scale(1.15)
        eq3 = MathTex("x-y+2z=5").scale(1.15)

        equations = VGroup(eq1, eq2, eq3).arrange(
            DOWN, buff=0.65
        )
        equations.move_to(UP * 0.3)

        note = explanation(
            "Our goal is to find the unknown values x, y and z."
        )

        self.play(FadeIn(h))
        self.wait(6.2)

        self.play(Write(eq1))
        self.wait(0.5)

        self.play(Write(eq2))
        self.wait(2.8)

        self.play(Write(eq3))
        self.wait(3.2)

        self.play(FadeIn(note))
        self.wait(3.5)

        self.play(
            FadeOut(h),
            FadeOut(equations),
            FadeOut(note)
        )

        # ----------------------------------
        # 3. AUGMENTED MATRIX
        # ----------------------------------

        show_step(
            "STEP 1: AUGMENTED MATRIX",

            r"\left[\begin{array}{ccc|c}"
            r"\boxed{1}&1&1&6\\"
            r"2&1&-1&1\\"
            r"1&-1&2&5"
            r"\end{array}\right]",

            "Write the coefficients and constants into a matrix.",
            6
        )

        show_step(
            "UNDERSTANDING THE PIVOT",

            r"\boxed{1}\quad 1\quad 1\quad | \quad 6",

            "The first entry is our first pivot. We use it to eliminate entries below it.",
            5
        )

        # ----------------------------------
        # 4. FIRST ROW OPERATION
        # ----------------------------------

        show_step(
            "STEP 2: ELIMINATE THE FIRST COLUMN",

            r"R_2 \rightarrow R_2-2R_1",

            "Subtract twice the first row from the second row.",
            5
        )

        show_step(
            "AFTER THE FIRST OPERATION",

            r"\left[\begin{array}{ccc|c}"
            r"1&1&1&6\\"
            r"0&\boxed{-1}&-3&-11\\"
            r"1&-1&2&5"
            r"\end{array}\right]",

            "The first entry in row 2 is now zero.",
            5
        )

        # ----------------------------------
        # 5. SECOND ROW OPERATION
        # ----------------------------------

        show_step(
            "STEP 3: ELIMINATE THE THIRD ROW",

            r"R_3 \rightarrow R_3-R_1",

            "Subtract the first row from the third row.",
            5
        )

        show_step(
            "AFTER THE SECOND OPERATION",

            r"\left[\begin{array}{ccc|c}"
            r"1&1&1&6\\"
            r"0&\boxed{-1}&-3&-11\\"
            r"0&-2&1&-1"
            r"\end{array}\right]",

            "The first entry in row 3 is also zero.",
            5
        )

        # ----------------------------------
        # 6. THIRD ROW OPERATION
        # ----------------------------------

        show_step(
            "STEP 4: ELIMINATE THE SECOND COLUMN",

            r"R_3 \rightarrow R_3-2R_2",

            "Use row 2 to eliminate the negative two in row 3.",
            5
        )

        show_step(
            "AFTER THE THIRD OPERATION",

            r"\left[\begin{array}{ccc|c}"
            r"1&1&1&6\\"
            r"0&\boxed{-1}&-3&-11\\"
            r"0&0&\boxed{7}&21"
            r"\end{array}\right]",

            "The entries below the second pivot are now zero.",
            5
        )

        # ----------------------------------
        # 7. NORMALIZE THE LAST PIVOT
        # ----------------------------------

        show_step(
            "STEP 5: NORMALIZE THE LAST ROW",

            r"R_3 \rightarrow \frac{R_3}{7}",

            "Divide every element in row 3 by seven.",
            5
        )

        show_step(
            "ROW ECHELON FORM",

            r"\left[\begin{array}{ccc|c}"
            r"1&1&1&6\\"
            r"0&-1&-3&-11\\"
            r"0&0&\boxed{1}&3"
            r"\end{array}\right]",

            "We have reached row echelon form.",
            6
        )

        # ----------------------------------
        # 8. BACK SUBSTITUTION
        # ----------------------------------

        show_step(
            "STEP 6: BACK SUBSTITUTION",

            r"z=3",

            "The third row directly gives us z equals three.",
            5
        )

        show_step(
            "FINDING Y",

            r"-y-3z=-11",

            "Substitute z equals three into the second row.",
            5
        )

        show_step(
            "SIMPLIFY",

            r"-y-9=-11",

            "Add nine to both sides.",
            4
        )

        show_step(
            "SOLVING FOR Y",

            r"-y=-2",

            "Multiply both sides by negative one.",
            4
        )

        show_step(
            "VALUE OF Y",

            r"y=2",

            "We have found the second unknown.",
            5
        )

        show_step(
            "FINDING X",

            r"x+y+z=6",

            "Substitute y equals two and z equals three.",
            5
        )

        show_step(
            "SIMPLIFY",

            r"x+2+3=6",

            "Combine the known values.",
            4
        )

        show_step(
            "VALUE OF X",

            r"x=1",

            "We have found all three unknowns.",
            5
        )

        # ----------------------------------

        # ----------------------------------
        # WORKED EXAMPLE: CALCULATING THE ROW OPERATIONS
        # ----------------------------------

        show_step(
            "WORKED EXAMPLE: FIRST ROW",
            r"R_2 \leftarrow R_2-2R_1",
            "Subtract twice each entry of row 1 from row 2.",
            3.3
        )

        show_step(
            "CALCULATE THE FIRST ENTRY",
            r"2-2(1)=0",
            "The first entry becomes zero.",
            3.3
        )

        show_step(
            "CALCULATE THE SECOND ENTRY",
            r"1-2(1)=-1",
            "The second entry becomes negative one.",
            3.3
        )

        show_step(
            "CALCULATE THE THIRD ENTRY",
            r"-1-2(1)=-3",
            "The third entry becomes negative three.",
            3.3
        )

        show_step(
            "CALCULATE THE CONSTANT",
            r"1-2(6)=-11",
            "The constant becomes negative eleven.",
            3.3
        )

        show_step(
            "NEW SECOND ROW",
            r"R_2=[0,-1,-3,-11]",
            "This is our updated second row.",
            3.3
        )

        show_step(
            "WORKED EXAMPLE: THIRD ROW",
            r"R_3 \leftarrow R_3-R_1",
            "Subtract row 1 from row 3, entry by entry.",
            3.3
        )

        show_step(
            "UPDATED THIRD ROW",
            r"R_3=[0,-2,1,-1]",
            "The first entry is zero. We are ready for the next elimination.",
            3.3
        )

        show_step(
            "ELIMINATE THE SECOND COLUMN",
            r"R_3=R_3-2R_2",
            "Use the updated second row to eliminate the negative two.",
            3.3
        )

        show_step(
            "CALCULATE THE FIRST ENTRY",
            r"0-2(0)=0",
            "The first entry remains zero.",
            3.3
        )

        show_step(
            "CALCULATE THE SECOND ENTRY",
            r"-2-2(-1)=0",
            "The second entry becomes zero.",
            3.3
        )

        show_step(
            "CALCULATE THE THIRD ENTRY",
            r"1-2(-3)=7",
            "The third entry becomes seven.",
            3.3
        )

        show_step(
            "CALCULATE THE CONSTANT",
            r"-1-2(-11)=21",
            "The constant becomes twenty-one.",
            3.3
        )

        show_step(
            "FINAL ROW",
            r"R_3=(0,0,7,21)",
            "The last row gives 7z equals 21, so z equals 3.",
            3.3
        )

        # 9. VERIFY THE SOLUTION
        # ----------------------------------

        h = heading("STEP 7: VERIFY OUR ANSWER")

        checks = VGroup(
            MathTex("1+2+3=6"),
            MathTex("2(1)+2-3=1"),
            MathTex("1-2+2(3)=5")
        ).arrange(DOWN, buff=0.55)

        checks.scale(0.9)
        checks.move_to(UP * 0.25)

        note = explanation(
            "All three original equations are satisfied!"
        )

        self.play(FadeIn(h))
        self.play(
            LaggedStart(
                *[Write(e) for e in checks],
                lag_ratio=0.7
            )
        )
        self.play(FadeIn(note))
        self.wait(7)

        self.play(
            FadeOut(h),
            FadeOut(checks),
            FadeOut(note)
        )

        # ----------------------------------
        # 10. FINAL SOLUTION
        # ----------------------------------

        final_title = Text(
            "FINAL SOLUTION",
            color="#F4C96B",
            font_size=34,
            weight=BOLD
        ).move_to(UP * 1.3)

        answer = MathTex(
            r"x=1,\qquad y=2,\qquad z=3",
            color="#7CFFB2"
        ).scale(1.1).move_to(ORIGIN)

        thanks = Text(
            "Gaussian Elimination Complete!",
            color=WHITE,
            font_size=22
        ).move_to(DOWN * 1.3)

        self.play(Write(final_title))
        self.play(Write(answer))
        self.play(FadeIn(thanks))
        self.wait(8)

        self.play(
            FadeOut(final_title),
            FadeOut(answer),
            FadeOut(thanks)
        )
