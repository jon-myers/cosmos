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
abjad.persist.as_png(lilypond_file, "./notation/example_1.png")


layer_1_durs = [abjad.Duration(3, 8) for i in range(4)]
layer_2_durs = [abjad.Duration(1, 8) for i in range(12)]
layer_3_durs = [abjad.Duration(1, 16) for i in range(24)]
layer_1_notes = [abjad.Note.from_pitch_and_duration("c''", dur) for dur in layer_1_durs]
layer_2_notes = [abjad.Note.from_pitch_and_duration("a'", dur) for dur in layer_2_durs]
layer_3_notes = [abjad.Note.from_pitch_and_duration("f'", dur) for dur in layer_3_durs]
staff_1 = abjad.Staff(layer_1_notes)
time_signature = abjad.TimeSignature((12, 8))


staff_2 = abjad.Staff(layer_2_notes)
staff_3 = abjad.Staff(layer_3_notes)
staff_group = abjad.StaffGroup([staff_1, staff_2, staff_3], lilypond_type="PianoStaff")

score = abjad.Score([staff_group], name="My Score")
abjad.attach(abjad.TimeSignature((12, 8)), score[0][0][0], context="StaffGroup")
# 12/8
# abjad.attach(time_signature, voice_1[0], context="Score")
# staff = abjad.Staff([voice_1, voice_2, voice_3], simultaneous=True)
setting = """ \\header { \n tagline = "" \n}                       /
\\paper { \n #(set-paper-size "a7landscape") \n} """

lilypond_file = abjad.LilyPondFile([setting, score])
abjad.persist.as_png(lilypond_file, "./notation/example_2.png")


# shuffle
time_signature = abjad.TimeSignature((12, 8))
hihat_durs = [abjad.Duration(1, 8) for i in range(12)]
hihat_notes = [abjad.Note.from_pitch_and_duration("f''", dur) for dur in hihat_durs]
override = abjad.LilyPondLiteral(r"\override NoteHead.style = #'cross")
# stem up
stem_override = abjad.LilyPondLiteral(r"\stemUp")
abjad.attach(stem_override, hihat_notes[0])
abjad.attach(time_signature, hihat_notes[0])
abjad.attach(override, hihat_notes[0])

kick_snare_durs = [(1, 4), (1, 8), (1, 4), (1, 8), (1, 4), (1, 8), (1, 4), (1, 8)]
kick_snare_notes = ["e'", "e'", "b'", "e'", "e'", "e'", "b'", "e'"]
kick_snare_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(kick_snare_notes, kick_snare_durs)]
# fifth note is actually a rest
kick_snare_notes[4] = abjad.Rest(kick_snare_notes[4].written_duration)

stem_override = abjad.LilyPondLiteral(r"\stemDown")
abjad.attach(stem_override, kick_snare_notes[0])
voice_1 = abjad.Voice(hihat_notes)
voice_2 = abjad.Voice(kick_snare_notes)
staff = abjad.Staff([voice_1, voice_2], simultaneous=True)
score = abjad.Score([staff], name="My Score")
setting = """ \\header { \n tagline = "" \n}                       /
\\paper { \n #(set-paper-size "a7landscape") \n} """

lilypond_file = abjad.LilyPondFile([setting, score])
abjad.persist.as_png(lilypond_file, "./notation/example_3.png")


# rock beat 4/4
hihat_durs = [abjad.Duration(1, 8) for i in range(8)]
hihat_notes = [abjad.Note.from_pitch_and_duration("f''", dur) for dur in hihat_durs]
override = abjad.LilyPondLiteral(r"\override NoteHead.style = #'cross")
stem_override = abjad.LilyPondLiteral(r"\stemUp")
abjad.attach(stem_override, hihat_notes[0])
abjad.attach(override, hihat_notes[0])
kick_snare_durs = [(1, 4) for i in range(4)]
kick_snare_notes = ["e'", "b'", "e'", "b'"]
kick_snare_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(kick_snare_notes, kick_snare_durs)]
stem_override = abjad.LilyPondLiteral(r"\stemDown")
abjad.attach(stem_override, kick_snare_notes[0])
voice_1 = abjad.Voice(hihat_notes)
voice_2 = abjad.Voice(kick_snare_notes)
staff = abjad.Staff([voice_1, voice_2], simultaneous=True)
score = abjad.Score([staff], name="My Score")
setting = """ \\header { \n tagline = "" \n}                       /
\\paper { \n #(set-paper-size "a7landscape") \n} """
lilypond_file = abjad.LilyPondFile([setting, score])
abjad.persist.as_png(lilypond_file, "./notation/example_4.png")

# rock beat 4/4 w/ bongo pattern
hihat_durs = [abjad.Duration(1, 8) for i in range(8)]
hihat_notes = [abjad.Note.from_pitch_and_duration("f''", dur) for dur in hihat_durs]
override = abjad.LilyPondLiteral(r"\override NoteHead.style = #'cross")
stem_override = abjad.LilyPondLiteral(r"\stemUp")
abjad.attach(stem_override, hihat_notes[0])
abjad.attach(override, hihat_notes[0])
kick_snare_durs = [(1, 4) for i in range(4)]
kick_snare_notes = ["e'", "b'", "e'", "b'"]
kick_snare_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(kick_snare_notes, kick_snare_durs)]
stem_override = abjad.LilyPondLiteral(r"\stemDown")
abjad.attach(stem_override, kick_snare_notes[0])
voice_1 = abjad.Voice(hihat_notes)
voice_2 = abjad.Voice(kick_snare_notes)
staff_1 = abjad.Staff([voice_1, voice_2], simultaneous=True)
bongo_durs = [(3, 8), (1, 4), (1, 8), (1, 4)]
bongo_notes = ["b'", "b'", "b'", "b'"]
bongo_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(bongo_notes, bongo_durs)]
bongo_notes[0] = abjad.Rest(bongo_notes[0].written_duration)

staff_2 = abjad.Staff(bongo_notes)
staff_group_ = abjad.StaffGroup([staff_1, staff_2])
abjad.attach(abjad.Repeat(), staff_group_)
score = abjad.Score([staff_group_])
setting = """ \\header { \n tagline = "" \n}                       /
\\paper { \n #(set-paper-size "a7landscape") \n} """
lilypond_file = abjad.LilyPondFile([setting, score])
abjad.persist.as_png(lilypond_file, "./notation/example_5.png")

# rock beat 4/4 with 3 bongo patterns
hihat_durs = [abjad.Duration(1, 8) for i in range(8)]
hihat_notes = [abjad.Note.from_pitch_and_duration("f''", dur) for dur in hihat_durs]
override = abjad.LilyPondLiteral(r"\override NoteHead.style = #'cross")
stem_override = abjad.LilyPondLiteral(r"\stemUp")
abjad.attach(stem_override, hihat_notes[0])
abjad.attach(override, hihat_notes[0])
kick_snare_durs = [(1, 4) for i in range(4)]
kick_snare_notes = ["e'", "b'", "e'", "b'"]
kick_snare_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(kick_snare_notes, kick_snare_durs)]
stem_override = abjad.LilyPondLiteral(r"\stemDown")
abjad.attach(stem_override, kick_snare_notes[0])
voice_1 = abjad.Voice(hihat_notes)
voice_2 = abjad.Voice(kick_snare_notes)
staff_1 = abjad.Staff([voice_1, voice_2], simultaneous=True)


bongo_durs = [(3, 8), (1, 4), (1, 8), (1, 4)]
bongo_notes = ["b'", "b'", "b'", "b'"]
bongo_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(bongo_notes, bongo_durs)]
bongo_notes[0] = abjad.Rest(bongo_notes[0].written_duration)
staff_2 = abjad.Staff(bongo_notes)

bongo_durs = [(1, 8), (1, 8), (1, 4), (1, 8), (1, 4), (1, 8)]
bongo_notes = ["b'" for i in range(len(bongo_durs))]
bongo_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(bongo_notes, bongo_durs)]
bongo_notes[0] = abjad.Rest(bongo_notes[0].written_duration)
staff_3 = abjad.Staff(bongo_notes)

bongo_durs = [(1, 4), (1, 8), (1, 4), (1, 8), (1, 8), (1, 8)]
bongo_notes = ["b'" for i in range(len(bongo_durs))]
bongo_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(bongo_notes, bongo_durs)]
staff_4 = abjad.Staff(bongo_notes)
staff_group = abjad.StaffGroup([staff_1, staff_2, staff_3, staff_4])
abjad.attach(abjad.Repeat(), staff_group)
score = abjad.Score([staff_group])
setting = """ \\header { \n tagline = "" \n}                       /
\\paper { \n #(set-paper-size "a7landscape") \n} """
lilypond_file = abjad.LilyPondFile([setting, score])
abjad.persist.as_png(lilypond_file, "./notation/example_6.png")



# 12/8 ghanaian 

agogo_durs = [(1, 4), (1, 8), (1, 8), (1, 8), (1, 8), (1, 8), (1, 4), (1, 4), (1, 8)]
agogo_notes = ["f''" for i in range(len(agogo_durs))]
agogo_notes[0] = "b'"
agogo_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(agogo_notes, agogo_durs)]
agogo_notes[2] = abjad.Rest(agogo_notes[3].written_duration)
agogo_notes[5] = abjad.Rest(agogo_notes[5].written_duration)
agogo_staff_1 = abjad.Staff(agogo_notes)
time_signature = abjad.TimeSignature((12, 8))
abjad.attach(time_signature, agogo_staff_1[0])
abjad.attach(abjad.Repeat(), agogo_staff_1)

agogo_durs = [(1, 4), (1, 8), (1, 8), (1, 8), (1, 8), (1, 8), (1, 4), (1, 4), (1, 8)]
agogo_notes = ["f''" for i in range(len(agogo_durs))]
agogo_notes[0] = "b'"
agogo_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(agogo_notes, agogo_durs)]
agogo_notes[0] = abjad.Rest(agogo_notes[0].written_duration)
agogo_notes[2] = abjad.Rest(agogo_notes[3].written_duration)
agogo_notes[5] = abjad.Rest(agogo_notes[5].written_duration)
agogo_staff_2 = abjad.Staff(agogo_notes)

agogo_staff_group = abjad.StaffGroup([agogo_staff_1, agogo_staff_2])
# have staff name next to staff

cymbal_durs = [(3, 8) for i in range(4)]
cymbal_notes = ["b'" for i in range(len(cymbal_durs))]
cymbal_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(cymbal_notes, cymbal_durs)]
cymbal_notes[0] = abjad.Rest(cymbal_notes[0].written_duration)
cymbal_staff = abjad.Staff(cymbal_notes)

thud_durs = [(1, 8) for i in range(12)]
thud_notes = ["b'" for i in range(len(thud_durs))]
thud_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(thud_notes, thud_durs)]
thud_notes[0] = abjad.Rest(thud_notes[0].written_duration)
thud_notes[3] = abjad.Rest(thud_notes[3].written_duration)
thud_notes[6] = abjad.Rest(thud_notes[6].written_duration)
thud_notes[9] = abjad.Rest(thud_notes[9].written_duration)
thud_staff_1 = abjad.Staff(thud_notes)

thud_durs = [(1, 8), (1, 16), (1, 16), (1, 8), (1, 8), (1, 8), (1, 8), (1, 8), (1, 16), (1, 16), (1, 8), (1, 8), (1, 8), (1, 8)]
thud_notes = ["b'" for i in range(len(thud_durs))]
thud_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(thud_notes, thud_durs)]
thud_notes[0] = abjad.Rest(thud_notes[0].written_duration)
thud_notes[3] = abjad.Rest(thud_notes[3].written_duration)
thud_notes[7] = abjad.Rest(thud_notes[7].written_duration)
thud_notes[10] = abjad.Rest(thud_notes[10].written_duration)
thud_staff_2 = abjad.Staff(thud_notes)

thud_durs = [(1, 8), (1, 16), (1, 16), (1, 8), (1, 16), (1, 16),(1, 8), (1, 16), (1, 16),(1, 8), (1, 16), (1, 16),(1, 8), (1, 16), (1, 16),(1, 8), (1, 16), (1, 16)]
thud_notes = ["b'" for i in range(len(thud_durs))]
thud_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(thud_notes, thud_durs)]
thud_notes[0] = abjad.Rest(thud_notes[0].written_duration)
thud_notes[3] = abjad.Rest(thud_notes[3].written_duration)
thud_notes[6] = abjad.Rest(thud_notes[6].written_duration)
thud_notes[9] = abjad.Rest(thud_notes[9].written_duration)
thud_notes[12] = abjad.Rest(thud_notes[12].written_duration)
thud_notes[15] = abjad.Rest(thud_notes[15].written_duration)
thud_staff_3 = abjad.Staff(thud_notes)

thud_staff_group = abjad.StaffGroup([thud_staff_1, thud_staff_2, thud_staff_3])


bongo_durs = [(1, 4), (1, 16), (1, 16), 
              (1, 16), (1, 16), (1, 4), 
              (1, 16), (1, 16), (1, 16), (1, 16), (1, 8), 
              (1, 8), (1, 16), (1, 16), (1, 16), (1, 16)]
bongo_notes = ["b'" for i in range(len(bongo_durs))]
bongo_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(bongo_notes, bongo_durs)]
bongo_notes[0] = abjad.Rest(bongo_notes[0].written_duration)
bongo_notes[5] = abjad.Rest(bongo_notes[5].written_duration)
bongo_notes[10] = abjad.Rest(bongo_notes[10].written_duration)
bongo_notes[11] = abjad.Rest(bongo_notes[11].written_duration)
bongo_staff_1 = abjad.Staff(bongo_notes)

bongo_durs = [(1, 4), (1, 16), (1, 16), 
              (1, 16), (1, 16), (1, 4), 
              (1, 16), (1, 16), (1, 16), (1, 16), (1, 8), 
              (1, 8), (1, 16), (1, 16), (1, 16), (1, 16)]
bongo_notes = ["b'" for i in range(len(bongo_durs))]
bongo_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(bongo_notes, bongo_durs)]
bongo_notes[0] = abjad.Rest(bongo_notes[0].written_duration)
bongo_notes[3] = abjad.Rest(bongo_notes[3].written_duration)
bongo_notes[5] = abjad.Rest(bongo_notes[5].written_duration)
bongo_notes[8] = abjad.Rest(bongo_notes[8].written_duration)
bongo_notes[10] = abjad.Rest(bongo_notes[10].written_duration)
bongo_notes[11] = abjad.Rest(bongo_notes[11].written_duration)
bongo_notes[14] = abjad.Rest(bongo_notes[14].written_duration)
bongo_staff_2 = abjad.Staff(bongo_notes)

bongo_durs = [(3, 4), 
              (1, 16), (1, 16), (1, 16), (1, 16), (1, 8), 
              (1, 8), (1, 16), (1, 16), (1, 16), (1, 16)]
bongo_notes = ["b'" for i in range(len(bongo_durs))]
bongo_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(bongo_notes, bongo_durs)]
bongo_notes[0] = abjad.Rest(bongo_notes[0].written_duration)
bongo_notes[5] = abjad.Rest(bongo_notes[5].written_duration)
bongo_notes[6] = abjad.Rest(bongo_notes[6].written_duration)
bongo_staff_3 = abjad.Staff(bongo_notes)

bongo_staff_group = abjad.StaffGroup([bongo_staff_1, bongo_staff_2, bongo_staff_3])

conga_durs = [(1, 8), (1, 8), (1, 8), 
              (1, 8), (1, 8), (1, 8),
              (1, 4), (1, 8),
              (1, 8), (1, 4)]
conga_notes = ["b'" for i in range(len(conga_durs))]
conga_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(conga_notes, conga_durs)]
conga_notes[2] = abjad.Rest(conga_notes[2].written_duration)
conga_notes[3] = abjad.Rest(conga_notes[3].written_duration)
conga_notes[6] = abjad.Rest(conga_notes[6].written_duration)
conga_notes[9] = abjad.Rest(conga_notes[9].written_duration)
conga_staff_1 = abjad.Staff(conga_notes)

conga_durs = [(1, 8), (1, 8), (1, 8), (3, 8), (3, 4)]
conga_notes = ["b'" for i in range(len(conga_durs))]
conga_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(conga_notes, conga_durs)]
conga_notes[2] = abjad.Rest(conga_notes[2].written_duration)
conga_notes[3] = abjad.Rest(conga_notes[3].written_duration)
conga_notes[4] = abjad.Rest(conga_notes[4].written_duration)
conga_staff_2 = abjad.Staff(conga_notes)

conga_durs = [(3, 8), 
              (1, 8), (1, 16), (1, 8), (1, 16), 
              (1, 4), (1, 16), (1, 16),
              (1, 16), (1, 16), (1, 4)]
conga_notes = ["b'" for i in range(len(conga_durs))]
conga_notes = [abjad.Note.from_pitch_and_duration(note, abjad.Duration(dur)) for note, dur in zip(conga_notes, conga_durs)]
conga_notes[0] = abjad.Rest(conga_notes[0].written_duration)
conga_notes[1] = abjad.Rest(conga_notes[1].written_duration)
conga_notes[5] = abjad.Rest(conga_notes[5].written_duration)
conga_notes[8] = abjad.Rest(conga_notes[8].written_duration)
conga_notes[10] = abjad.Rest(conga_notes[10].written_duration)
conga_staff_3 = abjad.Staff(conga_notes)


conga_staff_group = abjad.StaffGroup([conga_staff_1, conga_staff_2, conga_staff_3])




score = abjad.Score([agogo_staff_group, cymbal_staff, thud_staff_group, bongo_staff_group, conga_staff_group])
setting = """ \\header { \n tagline = "" \n}                       /
\\paper { \n #(set-paper-size "a4") \n} """
lilypond_file = abjad.LilyPondFile([setting, score])
abjad.persist.as_png(lilypond_file, "./notation/example_7.png")


# from Pillow import Image, ImageDraw, ImageOps
from PIL import Image, ImageDraw, ImageOps
def clean_img(path):
# Open input image
    im = Image.open(path)

    # Get rid of existing black border by flood-filling with white from top-left corner
    ImageDraw.floodfill(im,xy=(0,0),value=(255,255,255),thresh=10)

    # Get bounding box of text and trim to it
    bbox = ImageOps.invert(im).getbbox()
    trimmed = im.crop(bbox)

    # Add new white border, then new black, then new white border
    res = ImageOps.expand(trimmed, border=10, fill=(255,255,255))

    res.save(path)

clean_img('./notation/example_1.png')
clean_img('./notation/example_2.png')
clean_img('./notation/example_3.png')
clean_img('./notation/example_4.png')
clean_img('./notation/example_5.png')
clean_img('./notation/example_6.png')
clean_img('./notation/example_7.png')
