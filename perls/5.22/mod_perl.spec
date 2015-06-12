Name:           mod_perl
Version:        2.0.8
Release:        1%{?_dist}
Summary:        Embed a Perl interpreter in the Apache/2.x HTTP server
URL:            http://cpan.metacpan.org/authors/id/P/PH/PHRED/mod_perl-%{version}.tar.gz
License:        distributable
Group:          Development/Libraries

BuildRoot:      %{_tmppath}/%{name}-root
Source0:        mod_perl-%{version}.tar.gz




%description
Embed a Perl interpreter in the Apache/2.x HTTP server

##########################################################
%prep
%setup -q -n mod_perl-%{version}

%define __new_perl_provides %{_builddir}/cpan-perl-provides
cat > %{__new_perl_provides} <<END_PROVIDES
#!/bin/sh
# drop bad 'Provides' symbols
%{__perl_provides} $* | tee /tmp/out         |\
  sed -e '/^perl(Win32)$/d'                  |\
  sed -e '/^perl(Win32::.*)$/d'              |\
  sed -e '/^perl(Mac)$/d'                    |\
  sed -e '/^perl(Mac::.*)$/d'                |\
  sed -e '/^perl(warnings)$/d'               |\
  sed -e '/^perl(HTTP::Request::Common)$/d'  |\
  cat
END_PROVIDES
chmod +x %{__new_perl_provides}
%define __perl_provides %{__new_perl_provides}

%define __new_perl_requires %{_builddir}/cpan-perl-requires
cat > %{__new_perl_requires} <<END_REQUIRES
#!/bin/sh
# drop bad 'Requires' symbols
%{__perl_requires} $* | tee out2 |\
  sed -e '/^perl(Win32)$/d'                  |\
  sed -e '/^perl(Win32::.*)$/d'              |\
  sed -e '/^perl(Mac)$/d'                    |\
  sed -e '/^perl(Mac::.*)$/d'                |\
  sed -e '/^perl(Apache2::FunctionTable)$/d' |\
  sed -e '/^perl(Apache2::StructureTable)$/d'|\
  sed -e '/^perl(Apache::Test.*)$/d'         |\
  sed -e '/^perl(BSD::Resource)$/d'          |\
  sed -e '/^perl(Data::Flow)$/d'             |\
  sed -e '/^perl(Module::Build)$/d'          |\
  cat
END_REQUIRES
chmod +x %{__new_perl_requires}
%define __perl_requires %{__new_perl_requires}


##########################################################
%build
if [[ -f Makefile.PL ]]; then
  CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS=vendor
  make

elif [[ -f Build.PL ]]; then
  CFLAGS="$RPM_OPT_FLAGS" perl Build.PL --installdirs=vendor
  ./Build build

else
  echo "Error: No Makefile.PL or Build.PL found!!"
  exit 1

fi


##########################################################
%check
#make test


##########################################################
%clean
rm -rf $RPM_BUILD_ROOT


##########################################################
%install
rm -rf $RPM_BUILD_ROOT

if [[ -f Makefile.PL ]]; then
  make install DESTDIR=$RPM_BUILD_ROOT

elif [[ -f Build.PL ]]; then
  ./Build install --destdir=$RPM_BUILD_ROOT

else
  echo "Error: No Makefile.PL or Build.PL found!!"
  exit 1

fi

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -v {} \;
find $RPM_BUILD_ROOT/usr -type f -print | \
  sed "s@^$RPM_BUILD_ROOT@@g" > mod_perl-%{version}-files

if [ "x$(cat mod_perl-%{version}-files)" = "x" ] ; then
  echo "Error: No files found to package!!"
  exit 1

fi

%files -f mod_perl-%{version}-files
%defattr(-,root,root)

%changelog
* Fri Jun 12 2015 jhunt <jhunt@localhost.localdomain> 2.0.8-1
- Initial package, courtesy of cpanimal
