\version "2.20.0"
\language "english"
 \header { 
 tagline = "" 
}                       /
\paper { 
 #(set-paper-size "a4") 
} 
% OPEN_BRACKETS:
\new Score
<<
    % OPEN_BRACKETS:
    \new StaffGroup
    <<
        % BEFORE:
        % COMMANDS:
        \repeat volta 2
        % OPEN_BRACKETS:
        \new Staff
        {
            % OPENING:
            % COMMANDS:
            \time 12/8
            b'4
            f''8
            r8
            f''8
            f''8
            r8
            f''4
            f''4
            f''8
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            r4
            f''8
            r8
            f''8
            f''8
            r8
            f''4
            f''4
            f''8
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    >>
    % OPEN_BRACKETS:
    \new Staff
    {
        r4.
        b'4.
        b'4.
        b'4.
    % CLOSE_BRACKETS:
    }
    % OPEN_BRACKETS:
    \new StaffGroup
    <<
        % OPEN_BRACKETS:
        \new Staff
        {
            r8
            b'8
            b'8
            r8
            b'8
            b'8
            r8
            b'8
            b'8
            r8
            b'8
            b'8
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            r8
            b'16
            b'16
            r8
            b'8
            b'8
            b'8
            r8
            b'16
            b'16
            r8
            b'8
            b'8
            b'8
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            r8
            b'16
            b'16
            r8
            b'16
            b'16
            r8
            b'16
            b'16
            r8
            b'16
            b'16
            r8
            b'16
            b'16
            r8
            b'16
            b'16
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    >>
    % OPEN_BRACKETS:
    \new StaffGroup
    <<
        % OPEN_BRACKETS:
        \new Staff
        {
            r4
            b'16
            b'16
            b'16
            b'16
            r4
            b'16
            b'16
            b'16
            b'16
            r8
            r8
            b'16
            b'16
            b'16
            b'16
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            r4
            b'16
            b'16
            r16
            b'16
            r4
            b'16
            b'16
            r16
            b'16
            r8
            r8
            b'16
            b'16
            r16
            b'16
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            r2.
            b'16
            b'16
            b'16
            b'16
            r8
            r8
            b'16
            b'16
            b'16
            b'16
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    >>
    % OPEN_BRACKETS:
    \new StaffGroup
    <<
        % OPEN_BRACKETS:
        \new Staff
        {
            b'8
            b'8
            r8
            r8
            b'8
            b'8
            r4
            b'8
            b'8
            r4
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            b'8
            b'8
            r8
            r4.
            r2.
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            r4.
            r8
            b'16
            b'8
            b'16
            r4
            b'16
            b'16
            r16
            b'16
            r4
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    >>
% CLOSE_BRACKETS:
>>
