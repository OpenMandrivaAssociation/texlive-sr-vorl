# revision 32440
# category Package
# catalog-ctan /macros/latex/contrib/springer/sr-vorl
# catalog-date 2013-12-18 20:28:02 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-sr-vorl
Version:	1.0
Release:	2
Summary:	Class for Springer books
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/springer/sr-vorl
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sr-vorl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sr-vorl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sr-vorl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class provides a template for books to be published at
Springer Gabler, Vieweg or Springer Research. It may be used to
produce monographs in different formats and "several-authors-
books" fitting the conditions of Springer Gabler, Vieweg and
Springer Research.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sr-vorl/sr-vorl.cls
%doc %{_texmfdistdir}/doc/latex/sr-vorl/README
%doc %{_texmfdistdir}/doc/latex/sr-vorl/backmatter_sr-vorl.tex
%doc %{_texmfdistdir}/doc/latex/sr-vorl/frontmatter_sr-vorl.tex
%doc %{_texmfdistdir}/doc/latex/sr-vorl/hauptdatei_sr-vorl.tex
%doc %{_texmfdistdir}/doc/latex/sr-vorl/mainmatter_sr-vorl.tex
%doc %{_texmfdistdir}/doc/latex/sr-vorl/sr-vorl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sr-vorl/sr-vorl.dtx
%doc %{_texmfdistdir}/source/latex/sr-vorl/sr-vorl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
