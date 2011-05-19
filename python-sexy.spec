%define name python-sexy
%define version 0.1.9
%define release %mkrel 6
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
