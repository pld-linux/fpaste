Summary:	A simple tool for pasting info onto fpaste.org
Name:		fpaste
Version:	0.3.7.1
Release:	1
License:	GPL v3+
Group:		Applications/Networking
URL:		https://fedorahosted.org/fpaste/
Source0:	https://fedorahosted.org/released/fpaste/%{name}-%{version}.tar.bz2
# Source0-md5:	53201ed0fdd1b9f325c43178adcd8878
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is often useful to be able to easily paste text to the Fedora
Pastebin at <http://fpaste.org> and this simple script will do that
and return the resulting URL so that people may examine the output.
This can hopefully help folks who are for some reason stuck without X,
working remotely, or any other reason they may be unable to paste
something into the pastebin

%prep
%setup -q

%{__sed} -i -e '1s,^#!.*python,#!%{__python},' %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
