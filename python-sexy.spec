%define oname sexy-python

Summary:	Python bingings for the sexy GTK+ widgets
Name:		python-sexy
Version:	0.1.9
Release:	20
License:	LGPLv2
Group:		Development/Python
Url:		https://www.chipx86.com/wiki/Libsexy#sexy-python
Source0:	%{oname}-%{version}.tar.bz2
Patch0:		sexy-python-0.1.9-link.patch
BuildRequires:	pkgconfig(libsexy)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python2)
Requires:	pygtk2.0

%description
Sexy-python is a set of Python bindings around libsexy.

Libsexy is a collection of GTK+ widgets that extend the functionality
of such standard widgets as GtkEntry and GtkLabel by subclassing them
and working around the limitations of the widgets.

%prep
%setup -qn %{oname}-%{version}
%patch0 -p0

%build
export PYTHON=%{__python2}
%configure
%make

%install
%makeinstall_std

%files
%doc AUTHORS README NEWS
%{py2_platsitedir}/gtk-2.0/sexy.so
%{_datadir}/pygtk/2.0/defs/sexy.defs

