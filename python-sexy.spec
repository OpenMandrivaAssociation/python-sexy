%define name python-sexy
%define version 0.1.9
%define release 10
%define oname sexy-python

Summary: Python bingings for the sexy GTK+ widgets
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{version}.tar.bz2
Patch0: sexy-python-0.1.9-link.patch
License: LGPL
Group: Development/Python
Url: http://www.chipx86.com/wiki/Libsexy#sexy-python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pygtk2.0-devel
BuildRequires: libsexy-devel
Requires: pygtk2.0

%description
Sexy-python is a set of Python bindings around libsexy.

Libsexy is a collection of GTK+ widgets that extend the functionality
of such standard widgets as GtkEntry and GtkLabel by subclassing them
and working around the limitations of the widgets.

%prep
%setup -q -n %oname-%version
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%py_platsitedir/gtk-2.0/sexy.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README NEWS
%py_platsitedir/gtk-2.0/sexy.so
%_datadir/pygtk/2.0/defs/sexy.defs


%changelog
* Thu May 19 2011 Funda Wang <fwang@mandriva.org> 0.1.9-6mdv2011.0
+ Revision: 676116
- fix linkage

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.9-5
+ Revision: 668034
- mass rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.9-4mdv2011.0
+ Revision: 523877
- rebuilt for 2010.1

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 0.1.9-3mdv2009.1
+ Revision: 319756
- rebuild for new python

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.1.9-2mdv2009.0
+ Revision: 219583
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 0.1.9-1mdv2008.0
+ Revision: 62980
- Import python-sexy



* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 0.1.9-1mdv2008.0
- initial package
