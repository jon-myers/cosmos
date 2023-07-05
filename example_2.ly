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
    \new PianoStaff
    <<
        % OPEN_BRACKETS:
        \new Staff
        {
            % OPENING:
            % COMMANDS:
            \time 12/8
            c''4.
            c''4.
            c''4.
            c''4.
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            a'8
            a'8
            a'8
            a'8
            a'8
            a'8
            a'8
            a'8
            a'8
            a'8
            a'8
            a'8
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
            f'16
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    >>
% CLOSE_BRACKETS:
>>
