Summary:	Han character dictionary
Name:		eclectus-segment-redpng
Version:	0.2
Release:	%mkrel 1
Group:		Development/Python
License:	GPLv3+
URL:		http://code.google.com/p/eclectus/
Source0:	http://eclectus.googlecode.com/files/red.png-%{version}beta.tar.gz
BuildArch:	noarch
Requires:	eclectus
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
Eclectus is a small Han character dictionary especially designed for
learners of Chinese character based languages like Mandarin Chinese
or Japanese.

%prep
%setup -qn red.png-%{version}beta

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/eclectus/red.png/
cp -fr *.png %{buildroot}%{_datadir}/eclectus/red.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/eclectus/red.png
