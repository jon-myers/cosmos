\version "2.20.0"
\language "english"
 \header { 
 tagline = "" 
}                       /
\paper { 
 #(set-paper-size "a9landscape") 
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
            c''4
            c''4
            c''4
            c''4
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \new Staff
        {
            c''8
            c''8
            c''8
            c''8
            c''8
            c''8
            c''8
            c''8
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    >>
% CLOSE_BRACKETS:
>>
