Name:		texlive-sr-vorl
Version:	59333
Release:	2
Summary:	Class for Springer books
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/springer/sr-vorl
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sr-vorl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sr-vorl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sr-vorl.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/sr-vorl
%doc %{_texmfdistdir}/doc/latex/sr-vorl
#- source
%doc %{_texmfdistdir}/source/latex/sr-vorl

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
