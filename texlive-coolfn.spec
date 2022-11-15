Name:		texlive-coolfn
Version:	64639
Release:	1
Summary:	Typeset long legal footnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coolfn
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coolfn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coolfn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides formatting for footnotes in long legal
documents, using hanging indents to make them look nicer.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/coolfn
%doc %{_texmfdistdir}/doc/latex/coolfn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
