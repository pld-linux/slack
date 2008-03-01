#
Summary:	Slack - configuration management system
Name:		slack
Version:	0.15.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.sundell.net/~alan/projects/slack/%{name}-%{version}.tar.gz
# Source0-md5:	500e76c68f6ed3526be31288520bd587
URL:		http://www.sundell.net/~alan/projects/slack/
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Slack is a configuration management system designed to appeal to lazy
admins. It's an evolution from the usual "put files in some central
directory" that is faily common practice. It's descended from an
earlier system I also wrote, called "subsets", and uses a multi-stage
rsync to fix some of the problems I had there.

Slack tries to allow centralized configuration management with a bare
minimum of effort. Usually, just putting a file in the right place
will cause the right thing to be done. It uses rsync to copy files
around, so can use any sort of source (NFS directory, remote server
over SSH, remote server over rsync) that rsync supports.

Basically, it's a glorified wrapper around rsync.

%prep
%setup -q

%build

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README TODO COPYING doc/%{name}-intro

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}*
%attr(755,root,root) %{_sbindir}/%{name}*
%{_libdir}/%{name}
%{_mandir}/man*/%{name}*
