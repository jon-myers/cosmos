\version "2.20.0"
\language "english"
 \header { 
 tagline = "" 
}                       /
\paper { 
 #(set-paper-size "a7landscape") 
} 
% OPEN_BRACKETS:
\new Score
<<
    % BEFORE:
    % COMMANDS:
    \repeat volta 2
    % OPEN_BRACKETS:
    \new StaffGroup
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
                b'4
                e'4
                b'4
            % CLOSE_BRACKETS:
            }
        % CLOSE_BRACKETS:
        >>
        % OPEN_BRACKETS:
        \new Staff
        {
            r4.
            b'4
            b'8
            b'4
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            r8
            b'8
            b'4
            b'8
            b'4
            b'8
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            b'4
            b'8
            b'4
            b'8
            b'8
            b'8
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    >>
% CLOSE_BRACKETS:
>>
