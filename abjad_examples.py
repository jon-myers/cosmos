import abjad

layer_1_durs = [abjad.Duration(1, 4) for i in range(4)]
layer_2_durs = [abjad.Duration(1, 8) for i in range(8)]
layer_1_notes = [abjad.Note.from_pitch_and_duration("c''", dur) for dur in layer_1_durs]
layer_2_notes = [abjad.Note.from_pitch_and_duration("c''", dur) for dur in layer_2_durs]
layer_1_staff = abjad.Staff(layer_1_notes)
layer_2_staff = abjad.Staff(layer_2_notes)
staff = abjad.StaffGroup([layer_1_staff, layer_2_staff], lilypond_type="PianoStaff")
score = abjad.Score([staff], name="My Score")
setting = """ \\header { \n tagline = "" \n}                       /
\\paper { \n #(set-paper-size "a9landscape") \n} """

lilypond_file = abjad.LilyPondFile([setting, score])
abjad.persist.as_png(lilypond_file, "./example_1.png")

