%global tl_name sr-vorl
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Class for Springer books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/springer/sr-vorl
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sr-vorl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sr-vorl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sr-vorl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX class and templates for books to be
published at Springer Gabler Research, Springer Vieweg Research,
Springer Spektrum Research, Springer VS Research, or Springer VS
Forschung. It may be used to produce monographs in different formats and
"several-authors-books" fitting the conditions of the aforementioned
publishers.

