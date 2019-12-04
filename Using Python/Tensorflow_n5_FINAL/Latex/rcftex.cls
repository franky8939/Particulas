%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Class rcftex.cls  v 2.0 (Sept. 2011)                 %%
%% A document class for Rev. Cub. Fis.                 %%
%%                                                     %%
%% Written by R. Cuan (rcuan@fisica.uh.cu)             %%
%% Faculty of Physics, Havana University.              %%
%%                                                     %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\ProvidesClass{rcftex}[25/10/2011 V 2.0]
\typeout{A document class for Rev. Cub. Fis.}
\typeout{Written by R. Cuan (rcuan@fisica.uh.cu)}
\typeout{Faculty of Physics, Havana University.}

\NeedsTeXFormat{LaTeX2e}[1995/12/01]

\newif\if@ES
\newif\if@EN

\newif\if@short

\@EStrue
\@ENfalse
\@shortfalse

\DeclareOption{ES}{\@EStrue\@ENfalse}
\DeclareOption{EN}{\@ENtrue\@ESfalse}
\DeclareOption{short}{\@shorttrue}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}%
                \typeout{Unknown option: passing ``\CurrentOption"
                         option on to the standard LaTeX article class.}}
\ProcessOptions

\LoadClass[10pt,letterpaper,twoside]{article}

%\RequirePackage{MinionPro}
\RequirePackage[letterpaper]{geometry}
\RequirePackage[]{xcolor}
\RequirePackage{multicol}
\RequirePackage[fleqn,intlimits]{amsmath}
%\RequirePackage{marginnote}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\pagestyle{fancy}

%\DeclareSymbolFont{operators}{OT1}{cmr}{m}{n}
%\DeclareSymbolFont{letters}{OML}{cmm}{m}{it}
%\DeclareSymbolFont{symbols}{OMS}{cmsy}{m}{n}
%\DeclareSymbolFont{largesymbols}{OMX}{cmex}{m}{n}

%%%%%%%%%%%%% Sizes %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Top
\setlength{\parindent}{0pt}
\setlength{\headheight}{12pt}
\setlength{\topmargin}{0pt}
\setlength{\headsep}{0pt}
\setlength{\voffset}{-2cm}


\setlength{\textheight}{25.5cm}

% Left
\setlength{\marginparsep}{22pt}
\setlength{\marginparwidth}{35pt}

\setlength{\marginparpush}{0pt}

\setlength{\oddsidemargin}{43pt} 
\setlength{\evensidemargin}{56pt} 

\setlength{\hoffset}{-1in}
\setlength{\textwidth}{18.1cm}

\setlength{\mathindent}{0pt} 

%%%%%%%%%%%%% Useful Commands %%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Editorial

\newcommand{\the@volume}{\#}
\newcommand{\vol}[1]{\renewcommand{\the@volume}{#1}}

\newcommand{\the@number}{\#}
\newcommand{\num}[1]{\renewcommand{\the@number}{#1}}

\newcommand{\the@year}{Mes 20\#\#}
\newcommand{\thedate}[1]{\renewcommand{\the@year}{#1}}

\newcommand{\page}[1]{\setcounter{page}{#1}}

\newcommand{\the@status}{MANUSCRITO}
\newcommand{\status}[1]{\renewcommand{\the@status}{\MakeUppercase{#1}}}

\newcommand{\the@received}{\#\#/\#\#/20\#\#}
\newcommand{\the@approved}{\#\#/\#\#/20\#\#}
\newcommand{\received}[1]{\renewcommand{\the@received}{#1}}
\newcommand{\approved}[1]{\renewcommand{\the@approved}{#1}}

% Spaces 

\newcommand{\easyspace}[1]{{\color{white}\rule{10pt}{1pt}}\par\vspace*{#1mm}} %% If \vspace doesn't work
\newcommand{\spacefree}[1]{\par\vspace{#1mm}{\color{white}\rule{10pt}{1pt}}\par} %% Same
\newcommand{\spacing}[1]{\renewcommand{\baselinestretch}{#1}\large\small} %% Interlined 

% Math enviroment

\renewcommand\theequation{$\arabic{equation}$}
\def\tagform@#1{\maketag@@@{(\ignorespaces#1\unskip\@@italiccorr)}} %\hspace*{7.6mm}}}
\def\@eqnnum{{\normalfont\normalcolor \tagform@\theequation}}


% Title & Author stuff
\newcommand{\the@title}{The title}
\renewcommand{\title}[1]{\renewcommand{\the@title}{\uppercase{#1}}}

\newcommand{\the@titleEN}{The title}
\newcommand{\titleEN}[1]{\renewcommand{\the@titleEN}{\uppercase{#1}}}

\newcommand{\the@author}{A. Author}          
\renewcommand{\author}[1]{\renewcommand{\the@author}{#1}}

%%%%%%%%%%%%%%%%%% The Affiliation %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\toaff}[1]{{\small\selectfont\textsuperscript{#1}\fontshape{sc}\normalsize}}
\newcommand{\emailto}{\dag}
\newcommand{\emailtosp}{\dag~}

\newcommand{\the@affiliations}{Affiliations}          
\newcommand{\affiliations}[1]{\renewcommand{\the@affiliations}{#1}} 

\newcounter{numbaff}      
\setcounter{numbaff}{0}                                   
\newcommand{\aff}{\par\stepcounter{numbaff} \alph{numbaff}) }      

\newcommand{\the@email}{\vspace{-2pt} {\footnotesize \dag~autor para la correspondencia}}

\newenvironment{putaff}{
                       \footnotesize
                       \selectfont
          
                       }{
                       \par
                       \vspace{-1pt}
                       \the@email
                       }

\if@ES
     \newcommand{\put@key}{Palabras Clave.}
\else
     \newcommand{\put@key}{Key Words.}
\fi

%%%%%%%%%%%% The Abstracts %%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\the@abstractES}{Resumen en Espa\~{n}ol.}
\newcommand{\abstractES}[1]{\renewcommand{\the@abstractES}{#1}}

\newcommand{\the@abstractEN}{Abstract in English.}
\newcommand{\abstractEN}[1]{\renewcommand{\the@abstractEN}{#1}}

\newcommand{\the@keyW}{Key words.}
\newcommand{\keyW}[1]{\renewcommand{\the@keyW}{#1}}

\newenvironment{the@abstract}{
                           \easyspace{-4.1}
                           \rule{\textwidth}{.5pt}\par
                           \vspace*{-3mm}
                           \begin{multicols}{2}
                           \spacing{0.9}
                           \small
                           \selectfont
                           }{
                           \end{multicols} 
                           \par
                           \vspace*{-4.8mm} 
                           \rule{\textwidth}{.5pt}\par                          
                           }

%%%%%%%%%%%% AtBegin & AtEnd%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\AtBeginDocument{
  \easyspace{-3}%\clearpage
  \noindent\rule{\textwidth}{3pt}\par
  \vspace*{-2pt} 
  {\footnotesize\selectfont\noindent \hfill \the@status}\par
  \vspace*{-7pt}
  \noindent\rule{\textwidth}{1pt}\par
  
}

\AtEndDocument{
   \end{multicols}
   \rule{\linewidth}{12.5pt}    
}

\if@short

\renewcommand{\maketitle}{
          \vspace*{2.4mm}
          {\LARGE\selectfont\noindent \the@title}\par \vspace{3mm}
          {\LARGE\selectfont\noindent \the@titleEN}\par
          \vspace*{6.5mm}
          {\fontshape{sc}\large\selectfont\noindent \the@author}\par
          \vspace*{6mm}
          \begin{putaff}
              \the@affiliations
          \end{putaff}
          \par
          \vspace*{4.2mm}
          {\fontseries{b}\small\selectfont\noindent \put@key } {\small\selectfont \the@keyW}\par
          \vspace*{2mm}
          \begin{multicols}{2} 
          \setlength{\parskip}{10pt}
          } 
          
\else

\renewcommand{\maketitle}{
          \vspace*{2.4mm}
          {\LARGE\selectfont\noindent \the@title}\par \vspace{3mm}
          {\LARGE\selectfont\noindent \the@titleEN}\par
          \vspace*{6.5mm}
          {\fontshape{sc}\large\selectfont\noindent \the@author}\par
          \vspace*{6mm}
          \begin{putaff}
              \the@affiliations
          \end{putaff}

          \begin{the@abstract}
              \parbox{\linewidth}{\the@abstractES}\columnbreak
              \par
              \parbox{\linewidth}{\the@abstractEN}\par
          \end{the@abstract}\par
          \vspace*{4.2mm}
          {\fontseries{b}\small\selectfont\noindent \put@key } {\small\selectfont \the@keyW}\par
          \vspace*{2mm}
          \begin{multicols}{2} 
          \setlength{\parskip}{10pt}
          } 
          
\fi


%%%%%%%%%%%%%%%%%%%%%%%%% Section %%%%%%%%%%%%%%%%%%

\if@short

\renewcommand{\section}[1]{#1}
\renewcommand{\subsection}[1]{#1}
\renewcommand{\subsubsection}[1]{#1}

\else

\renewcommand{\section}[1]{\par {\large \uppercase{#1}}\par\vspace*{-2mm}}
\renewcommand{\subsection}[1]{\par{\itshape #1:\hspace{1ex}}}
\renewcommand{\subsubsection}[1]{#1}

\fi


%%%%%%%%%%%%%%%%%%%%%%%%% Lateral Notes %%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\renewcommand{\headrulewidth}{0pt} %Quita la raya 
\renewcommand{\footrulewidth}{0pt} 


%% Redefine the figure environment

\if@ES
   \newcommand{\the@figcapt}{Figura }
\else
   \newcommand{\the@figcapt}{Figure }
\fi

\newcommand{\the@caption}{}

\renewcommand{\caption}[1]{\renewcommand{\the@caption}{#1}}

\renewenvironment{figure}{
            \refstepcounter{figure}
            \par
            \centering
                         }{
            {\color{white}\rule{6.1cm}{1pt}}\par
            \vspace{-0.7cm}
            \flushleft 
            {\footnotesize\selectfont \the@figcapt \arabic{figure}.  \the@caption}
            \par
                         }

\def\@cite#1#2{{%\fontfamily{ptm}
\selectfont [#1]\if@tempswa , [#2]\fi}}


%% Define the table environment


\if@ES
  \newcommand{\the@tabcapt}{Tabla }
\else
  \newcommand{\the@tabcapt}{Table }
\fi

\newcommand{\tabhead}[2]{\hline
\multicolumn{#1}{|p{#2}|}{\small \hspace{2.9cm} \mbox{\the@tabcapt \Roman{table}} \hspace{2.9cm} \linebreak\the@caption}\\}

\newenvironment{tablenviroment}{
             \refstepcounter{table}
             \setlength{\arrayrulewidth}{0.8pt}
             \noindent
             \footnotesize
             \begin{center}
                               }{
             \end{center}
             \small
                               }



%% Redefine the Bibliography environment
\renewenvironment{thebibliography}[1]{
      {\rule{\linewidth}{.5pt}}
      \par\vspace*{-5mm}
      \setlength{\leftmargini}{0cm}
      \list{[$\@arabic\c@enumiv$] \hspace{-1.8mm}}{
           \@openbib@code 
           \usecounter{enumiv}%
           \let\p@enumiv\@empty
           \renewcommand\theenumiv{\@arabic\c@enumiv}
           }%
      \sloppy
      \sfcode`\.\@m 
      \small
      \setlength{\itemsep}{0cm}%
      \setlength{\parskip}{0cm}%
      \setlength{\itemindent}{0.45cm}
     }
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist}

