%global tl_name coolfn
%global tl_revision 69007

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.2
Release:	%{tl_revision}.1
Summary:	Typeset long legal footnotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/coolfn
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coolfn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coolfn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides formatting for footnotes in long legal documents,
using hanging indents to make them look nicer.

