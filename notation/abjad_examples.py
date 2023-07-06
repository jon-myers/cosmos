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
