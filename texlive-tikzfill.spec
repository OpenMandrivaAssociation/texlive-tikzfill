Name:		texlive-tikzfill
Version:	67847
Release:	1
Summary:	TikZ libraries for filling with images and patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tikzfill
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzfill.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzfill.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a collection of TikZ libraries which add further
options to fill TikZ paths with images and patterns. The
libraries comprise fillings with images from files and from
TikZ pictures. Also, patterns of hexagons and of rhombi are
provided.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikzfill
%doc %{_texmfdistdir}/doc/latex/tikzfill

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
