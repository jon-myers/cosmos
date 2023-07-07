\version "2.20.0"
\language "english"
 \header { 
 tagline = "" 
}                       /
\paper { 
 #(set-paper-size "a7landscape") 
} 
% OPEN_BRACKETS:
\context Score = "My Score"
<<
    % OPEN_BRACKETS:
    \new Staff
    <<
        % OPEN_BRACKETS:
        \new Voice
        {
            % BEFORE:
            % COMMANDS:
            \override NoteHead.style = #'cross
            \stemUp
            % OPENING:
            % COMMANDS:
            \time 12/8
            f''8
            f''8
            f''8
            f''8
            f''8
            f''8
            f''8
            f''8
            f''8
            f''8
            f''8
            f''8
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Voice
        {
            % BEFORE:
            % COMMANDS:
            \stemDown
            e'4
            e'8
            b'4
            e'8
            r4
            e'8
            b'4
            e'8
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    >>
% CLOSE_BRACKETS:
>>
