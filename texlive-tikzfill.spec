%global tl_name tikzfill
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.0
Release:	%{tl_revision}.1
Summary:	TikZ libraries for filling with images and patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzfill
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzfill.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzfill.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a collection of TikZ libraries which add further options to fill
TikZ paths with images and patterns. The libraries comprise fillings
with images from files and from TikZ pictures. Also, patterns of
hexagons and of rhombi are provided.

