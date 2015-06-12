%define perl_version    5.22.0
%define perl_epoch      4
%define perl_arch_stem -thread-multi
%define perl_archname %{_arch}-%{_os}%{perl_arch_stem}

%define multilib_64_archs x86_64 s390x ppc64 sparc64

Name:           perl
Version:        %{perl_version}
Release:        1%{?dist}
Epoch:          %{perl_epoch}
Summary:        Practical Extraction and Report Language
Group:          Development/Languages
# Modules Tie::File and Getopt::Long are licenced under "GPLv2+ or Artistic,"
# we have to reflect that in the sub-package containing them.
# under UCD are unicode tables
# Public domain: ext/SDBM_File/sdbm/*, ext/Compress-Raw-Bzip2/bzip2-src/dlltest.c 
# MIT: ext/MIME-Base64/Base64.xs 
# Copyright Only: for example ext/Text-Soundex/Soundex.xs 
License:        (GPL+ or Artistic) and (GPLv2+ or Artistic) and Copyright Only and MIT and Public Domain and UCD
Url:            http://www.perl.org/
Source0:        http://www.cpan.org/src/5.0/perl-%{perl_version}.tar.gz
Patch0:         perl-5.22.0-PAUSE.patch

# rpm vs cpan evaluate "bigger" release number differenty. Sometimes we need to
# change version according to rpm update (macro _rpm vs _real).
%define                     Archive_Tar_version 2.04
%define                     Compress_Raw_Bzip2_version 2.068
%define                     Compress_Raw_Zlib_version 2.068
%define                     Compress_Zlib_version 2.068
%define                     CPAN_version 2.11
%define                     Digest_SHA_version 5.95
%define                     ExtUtils_CBuilder_version 0.28
%define                     ExtUtils_Embed_version 1.32
%define                     ExtUtils_MakeMaker_version 7.04.01
%define                     ExtUtils_ParseXS_version 3.28
%define                     File_Fetch_version 0.48
%define                     File_Path_version 2.09
%define                     File_Temp_version 0.2304
%define                     IO_Compress_Base_version 2.068
%define                     IO_Compress_Bzip2_version 2.068
%define                     IO_Compress_Zlib_version 2.068
%define                     IO_Zlib_version 1.10
%define                     IPC_Cmd_version 0.92
%define                     Locale_Maketext_Simple_version 1.26
%define                     Module_CoreList_version 5.20150520
%define                     Module_Load_version 0.32
%define                     Module_Load_Conditional_version 0.64
%define                     Module_Loaded_version 0.08
%define                     Params_Check_version 0.38
%define                     Parse_CPAN_Meta_version 1.4414
%define                     Pod_Escapes_version 1.07
%define                     Pod_Simple_version 3.29
%define                     Test_Harness_version 3.35
%define                     Test_Simple_version 1.001014
%define                     Time_Piece_version 1.29
%define                     Time_HiRes_version 1.9726
%define                     threads_version 2.01
%define                     parent_version 0.232
%define                     version_version 0.9909

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  gcc
BuildRequires:  tcsh, dos2unix, man, groff
BuildRequires:  gdbm-devel, db4-devel, bzip2-devel, zlib-devel
# For tests
BuildRequires:  procps, rsyslog

# The long line of Perl provides.

# These provides are needed by the perl pkg itself with auto-generated perl.req
Provides: perl(VMS::Filespec)
Provides: perl(VMS::Stdio)

# Compat provides which helps to future changes to new versions
Provides: perl(:MODULE_COMPAT_5.22.0)
# To replace CentOS 6.x system packages
Provides: perl(:MODULE_COMPAT_5.10.0)
Provides: perl(:MODULE_COMPAT_5.10.1)

# Threading provides
Provides: perl(:WITH_ITHREADS)
Provides: perl(:WITH_THREADS)
# Largefile provides
Provides: perl(:WITH_LARGEFILES)
# PerlIO provides
Provides: perl(:WITH_PERLIO)
# File provides
Provides: perl(bytes_heavy.pl)
Provides: perl(dumpvar.pl)
Provides: perl(open3.pl)
Provides: perl(perl5db.pl)
Provides: perl(utf8_heavy.pl)
Provides: perl(Carp::Heavy)

# Parse_CPAN_Meta
Provides:  perl-Parse-CPAN-Meta = %{Parse_CPAN_Meta_version}
Obsoletes: perl-Parse-CPAN-Meta < %{Parse_CPAN_Meta_version}

# Long history in 3rd-party repositories:
Provides:  perl-File-Temp = %{File_Temp_version}
Obsoletes: perl-File-Temp < %{File_Temp_version}

# Use new testing module perl-Test-Harness, obsolete it outside of this package
Provides:  perl-TAP-Harness = %{Test_Harness_version}
Obsoletes: perl-TAP-Harness < %{Test_Harness_version}

Requires: perl-libs = %{perl_epoch}:%{perl_version}-%{release}

# Dropped since 5.10
Obsoletes: perl-suidperl
Obsoletes: perl-Archive-Extract
Obsoletes: perl-CPANPLUS
Obsoletes: perl-CGI
Obsoletes: perl-Log-Message
Obsoletes: perl-Log-Message-Simple
Obsoletes: perl-Module-Build
Obsoletes: perl-Module-Pluggable
Obsoletes: perl-Object-Accessor
Obsoletes: perl-Package-Constants
Obsoletes: perl-Term-UI

# We need this to break the dependency loop, and ensure that perl-libs 
# gets installed before perl.
Requires(post): perl-libs

%description
Perl is a high-level programming language with roots in C, sed, awk
and shell scripting.  Perl is good at handling processes and files,
and is especially good at handling text.  Perl's hallmarks are
practicality and efficiency.  While it is used to do a lot of
different things, Perl's most common applications are system
administration utilities and web programming.  A large proportion of
the CGI scripts on the web are written in Perl.  You need the perl
package installed on your system so that your system can handle Perl
scripts.

Install this package if you want to program in Perl or enable your
system to handle Perl scripts.

%package libs
Summary:        The libraries for the perl runtime
Group:          Development/Languages
License:        GPL+ or Artistic
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description libs
The libraries for the perl runtime


%package devel
Summary:        Header files for use in perl development
Group:          Development/Languages
License:        GPL+ or Artistic
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
# Require Config{libs} providers, bug #905482
Requires:       glibc-devel, gdbm-devel, db4-devel

%description devel
This package contains header files and development modules.
Most perl packages will need to install perl-devel to build.


%package Archive-Tar
Summary:        A module for Perl manipulation of .tar files
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Archive_Tar_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Compress::Zlib), perl(IO::Zlib)

%description Archive-Tar
Archive::Tar provides an object oriented mechanism for handling tar
files.  It provides class methods for quick and easy files handling
while also allowing for the creation of tar file objects for custom
manipulation.  If you have the IO::Zlib module installed, Archive::Tar
will also support compressed or gzipped tar files.


%package Compress-Raw-Bzip2
Summary:        Low-Level Interface to bzip2 compression library
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Compress_Raw_Bzip2_version}
Requires:       perl(XSLoader)

%description Compress-Raw-Bzip2
Compress::Raw::Bzip2 provides an interface to the in-memory
compression/uncompression functions from the bzip2 compression library.

Although the primary purpose for the existence of Compress::Raw::Bzip2 is for
use by the  IO::Compress::Bzip2 and IO::Compress::Bunzip2 modules, it can be
used on its own for simple compression/uncompression tasks.


%package Compress-Raw-Zlib
Summary:        Low-Level Interface to the zlib compression library
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          1
Version:        %{Compress_Raw_Zlib_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Compress-Raw-Zlib
This module provides a Perl interface to the zlib compression library.
It is used by IO::Compress::Zlib.


%package Compress-Zlib
Summary:        A module providing Perl interfaces to the zlib compression library
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Compress_Zlib_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Compress-Zlib
The Compress::Zlib module provides a Perl interface to the zlib
compression library. Most of the functionality provided by zlib is
available in Compress::Zlib.

The module can be split into two general areas of functionality,
namely in-memory compression/decompression and read/write access to
gzip files.


%package CPAN
Summary:        Query, download and build perl modules from CPAN sites
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        %{CPAN_version}
Requires:       perl(Digest::SHA)
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Provides:       cpan = %{version}

%description CPAN
Query, download and build perl modules from CPAN sites.


%package Digest-SHA
Summary:        Perl extension for SHA-1/224/256/384/512
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Digest_SHA_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Digest-SHA
Digest::SHA is a complete implementation of the NIST Secure Hash
Standard.  It gives Perl programmers a convenient way to calculate
SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 message digests.  The
module can handle all types of input, including partial-byte data.


%package ExtUtils-CBuilder
Summary:        Compile and link C code for Perl modules
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{ExtUtils_CBuilder_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description ExtUtils-CBuilder
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was
motivated by the Module::Build project, but may be useful for other
purposes as well.


%package ExtUtils-Embed
Summary:        Utilities for embedding Perl in C/C++ applications
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        %{ExtUtils_Embed_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description ExtUtils-Embed
Utilities for embedding Perl in C/C++ applications.


%package ExtUtils-MakeMaker
Summary:        Create a module Makefile
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
# It's really 6.55_02, but we drop the _02.
Version:        %{ExtUtils_MakeMaker_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Test::Harness)

%description ExtUtils-MakeMaker
Create a module Makefile.


%package ExtUtils-ParseXS
Summary:        Module and a script for converting Perl XS code into C code
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{ExtUtils_ParseXS_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description ExtUtils-ParseXS
ExtUtils::ParseXS will compile XS code into C code by embedding the
constructs necessary to let C functions manipulate Perl values and
creates the glue necessary to let Perl access those functions.


%package File-Fetch
Summary:        Generic file fetching mechanism
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{File_Fetch_version}
Requires:       perl(IPC::Cmd) >= 0.36
Requires:       perl(Module::Load::Conditional) >= 0.04
Requires:       perl(Params::Check) >= 0.07
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description File-Fetch
File::Fetch is a generic file fetching mechanism.


%package IO-Compress-Base
Summary:        Base Class for IO::Compress modules
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{IO_Compress_Base_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IO-Compress-Base
This module is the base class for all IO::Compress and IO::Uncompress
modules. This module is not intended for direct use in application
code. Its sole purpose is to to be sub-classed by IO::Compress
modules.


%package IO-Compress-Bzip2
Summary:        Perl interface to allow reading and writing of bzip2 data
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{IO_Compress_Bzip2_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IO-Compress-Bzip2
This module provides a Perl interface that allows writing/writing bzip2
compressed data to/from files or buffer.


%package IO-Compress-Zlib
Summary:        Perl interface to allow reading and writing of gzip and zip data
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{IO_Compress_Zlib_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IO-Compress-Zlib
This module provides an "IO::"-style Perl interface to "Compress::Zlib"


%package IO-Zlib
Summary:        Perl IO:: style interface to Compress::Zlib
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{IO_Zlib_version}
Requires:       perl(Compress::Zlib)
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IO-Zlib
This modules provides an IO:: style interface to the Compress::Zlib
package. The main advantage is that you can use an IO::Zlib object in
much the same way as an IO::File object so you can have common code
that doesn't know which sort of file it is using.


%package IPC-Cmd
Summary:        Finding and running system commands made easy
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
# do not upgrade in the future to _something version. They are testing!
Version:        %{IPC_Cmd_version}
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IPC-Cmd
IPC::Cmd allows you to run commands, interactively if desired, in a
platform independent way, but have them still work.


%package Locale-Maketext-Simple
Summary:        Simple interface to Locale::Maketext::Lexicon
Group:          Development/Libraries
License:        MIT
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Locale_Maketext_Simple_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Locale-Maketext-Simple
This module is a simple wrapper around Locale::Maketext::Lexicon, designed
to alleviate the need of creating Language Classes for module authors.


%package Module-CoreList
Summary:        Perl core modules indexed by perl versions
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Module_CoreList_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(version)

%description Module-CoreList
Module::CoreList contains the hash of hashes %Module::CoreList::version,
this is keyed on perl version as indicated in $].  The second level hash
is module => version pairs.


%package Module-Load
Summary:        Runtime require of both modules and files
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Module_Load_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Load
Module::Load eliminates the need to know whether you are trying to
require either a file or a module.


%package Module-Load-Conditional
Summary:        Looking up module information / loading at runtime
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Module_Load_Conditional_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Load-Conditional
Module::Load::Conditional provides simple ways to query and possibly 
load
any of the modules you have installed on your system during runtime.


%package Module-Loaded
Summary:        Mark modules as loaded or unloaded
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Module_Loaded_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Loaded
When testing applications, often you find yourself needing to provide
functionality in your test environment that would usually be provided by
external modules. Rather than munging the %INC by hand to mark these
external modules as loaded, so they are not attempted to be loaded by
perl, this module offers you a very simple way to mark modules as loaded
and/or unloaded.

%package Params-Check
Summary:        Generic input parsing/checking mechanism
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Params_Check_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Params-Check
Params::Check is a generic input parsing/checking mechanism.


%package Parse-CPAN-Meta
Summary:        Parse META.yml and other similar CPAN metadata files
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Parse_CPAN_Meta_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Parse-CPAN-Meta 
Parse::CPAN::Meta is a parser for META.yml files, based on the parser half
of YAML::Tiny.


%package Pod-Escapes
Summary:        Perl module for resolving POD escape sequences
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Pod_Escapes_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Pod-Escapes
This module provides things that are useful in decoding Pod E<...>
sequences. Presumably, it should be used only by Pod parsers and/or
formatters.


%package Pod-Simple
Summary:        Framework for parsing POD documentation
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Pod_Simple_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Pod-Simple
Pod::Simple is a Perl library for parsing text in the Pod ("plain old
documentation") markup language that is typically used for writing
documentation for Perl and for Perl modules.

%package Test-Harness
Summary:        Run Perl standard test scripts with statistics
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Test_Harness_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Test-Harness
Run Perl standard test scripts with statistics.
Use TAP::Parser, Test::Harness package was whole rewritten.

%package Test-Simple
Summary:        Basic utilities for writing tests
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Test_Simple_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Test-Simple
Basic utilities for writing tests.


%package Time-Piece
Summary:        Time objects from localtime and gmtime
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Time_Piece_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Time-Piece
The Time::Piece module replaces the standard localtime and gmtime functions
with implementations that return objects.  It does so in a backwards
compatible manner, so that using localtime or gmtime as documented in
perlfunc still behave as expected.


%package Time-HiRes
Summary:        High resolution alarm, sleep, gettimeofday, interval timers
Group:          Development/Libraries
License:        GPL+ or Artistic
Version:        %{Time_HiRes_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Time-HiRes
The Time::HiRes module implements a Perl interface to the usleep, nanosleep, 
ualarm, gettimeofday, and setitimer/getitimer system calls, in other words, 
high resolution time and timers. See the "EXAMPLES" section below and the test 
scripts for usage; see your system documentation for the description of the 
underlying nanosleep or usleep, ualarm, gettimeofday, and setitimer/getitimer
calls.


%package parent
Summary:        Establish an ISA relationship with base classes at compile time
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{parent_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description parent
parent allows you to both load one or more modules, while setting up 
inheritance from those modules at the same time. Mostly similar in 
effect to:

    package Baz;

    BEGIN {
        require Foo;
        require Bar; 
        
        push @ISA, qw(Foo Bar); 
    }

%package version
Summary:        Perl extension for Version Objects
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          3
Version:        %{version_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description version
Perl extension for Version Objects


%package core
Summary:        Base perl metapackage
Group:          Development/Languages
# This rpm doesn't contain any copyrightable material.
# Nevertheless, it needs a License tag, so we'll use the generic
# "perl" license.
License:        GPL+ or Artistic
Epoch:          0
Version:        %{perl_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-libs = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-devel = %{perl_epoch}:%{perl_version}-%{release}

Requires:       perl-Archive-Tar
Requires:       perl-Compress-Raw-Bzip2, perl-IO-Compress-Bzip2,
Requires:       perl-Compress-Raw-Zlib, perl-Compress-Zlib, perl-CPAN,
Requires:       perl-Digest-SHA, perl-ExtUtils-CBuilder,
Requires:       perl-ExtUtils-Embed, perl-ExtUtils-MakeMaker, perl-ExtUtils-ParseXS,
Requires:       perl-File-Fetch, perl-IO-Compress-Base, perl-IO-Compress-Zlib, perl-IO-Zlib,
Requires:       perl-IPC-Cmd, perl-Locale-Maketext-Simple,
Requires:       perl-Module-CoreList, perl-Module-Load,
Requires:       perl-Module-Load-Conditional, perl-Module-Loaded,
Requires:       perl-Params-Check, perl-Pod-Escapes, perl-Pod-Simple,
Requires:       perl-Test-Harness, perl-Test-Simple, perl-Time-Piece, perl-Time-HiRes, perl-version
Requires:       perl-parent, perl-Parse-CPAN-Meta

%description core
A metapackage which requires all of the perl bits and modules in the
upstream tarball from perl.org.


%prep
%setup -q
# Undo the "# hide me from PAUSE" hacks, so that 
# rpmbuild can find the Provides: for all modules
%patch -P0 -p1

echo "Setting up Provides: filter"
%define __new_perl_provides %{_builddir}/%{name}-%{perl_version}/rpmbuild-perl-provides
cat > %{__new_perl_provides} << END_PROVIDES
#!/bin/sh
# drop unversioned Provides:, since we have versioned ones
%{__perl_provides} $* |\
    sed -e '/^perl(Carp)$/d' |\
    sed -e '/^perl(Carp::Heavy)$/d' |\
    sed -e '/^perl(Config)$/d' |\
    sed -e '/^perl(DynaLoader)$/d' |\
    sed -e '/^perl(Locale::Maketext)$/d' |\
    sed -e '/^perl(Math::BigInt)$/d' |\
    sed -e '/^perl(Net::Config)$/d' |\
    sed -e '/^perl(Tie::Hash)$/d' |\
    sed -e '/^perl(bigint)$/d' |\
    sed -e '/^perl(bigrat)$/d' |\
    sed -e '/^perl(bytes)$/d' |\
    sed -e '/^perl(charnames)$/d' |\
    sed -e '/^perl(utf8)$/d' |\
    sed -e '/^perl(DB)$/d'
END_PROVIDES
chmod +x %{__new_perl_provides}
%define __perl_provides %{__new_perl_provides}

echo "Setting up Requires: filter"
%define __new_perl_requires %{_builddir}/%{name}-%{perl_version}/rpmbuild-perl-requires
cat > %{__new_perl_requires} << END_REQUIRES
#!/bin/sh
# drop bad Requires: (i.e. modules we don't want to advertise)
%{__perl_requires} $* |\
    sed -e '/^perl(unicore::Name)$/d' |\
    sed -e '/^perl(Mac::.*)$/d' |\
END_REQUIRES
chmod +x %{__new_perl_requires}
%define __perl_requires %{__new_perl_requires}

# Ensure that we never accidentally bundle zlib or bzip2
rm -rf ext/Compress-Raw-Zlib/zlib-src
rm -rf ext/Compress-Raw-Bzip2/bzip2-src
sed -i '/\(bzip2\|zlib\)-src/d' MANIFEST

%build
echo "RPM Build arch: %{_arch}"

# use "lib", not %{_lib}, for privlib, sitelib, and vendorlib
# To build production version, we would need -DDEBUGGING=-g

# Perl INC path (perl -V) in search order:
# - /usr/local/share/perl5            -- for CPAN     (site lib)
# - /usr/local/lib[64]/perl5          -- for CPAN     (site arch)
# - /usr/share/perl5/vendor_perl      -- 3rd party    (vendor lib)
# - /usr/lib[64]/perl5/vendor_perl    -- 3rd party    (vendor arch)
# - /usr/share/perl5                  -- RHEL         (priv lib)
# - /usr/lib[64]/perl5                -- RHEL         (arch lib)

%define privlib         %{_prefix}/share/perl5
%define archlib         %{_libdir}/perl5

/bin/sh Configure -des -Doptimize="$RPM_OPT_FLAGS" \
        -DDEBUGGING=-g \
        -Dversion=%{perl_version} \
        -Ddo_suid \
        -Dmyhostname=localhost \
        -Dperladmin=root@localhost \
        -Dcc='%{__cc}' \
        -Dcf_by='3Cinteractive' \
        -Dprefix=%{_prefix} \
        -Dvendorprefix=%{_prefix} \
        -Dsiteprefix=%{_prefix}/local \
        -Dsitelib="%{_prefix}/local/share/perl5" \
        -Dsitearch="%{_prefix}/local/%{_lib}/perl5" \
        -Dprivlib="%{privlib}" \
        -Darchlib="%{archlib}" \
        -Dvendorlib="%{privlib}/vendor_perl" \
        -Dvendorarch="%{archlib}/vendor_perl" \
        -Darchname=%{perl_archname} \
%ifarch %{multilib_64_archs}
        -Dlibpth="/usr/local/lib64 /lib64 %{_prefix}/lib64" \
%endif
%ifarch sparc sparcv9
        -Ud_longdbl \
%endif
        -Duseshrplib \
        -Dusethreads \
        -Duseithreads \
        -Duselargefiles \
        -Dd_semctl_semun \
        -Di_db \
        -Ui_ndbm \
        -Di_gdbm \
        -Di_shadow \
        -Di_syslog \
        -Dman3ext=3pm \
        -Duseperlio \
        -Dinstallusrbinperl=n \
        -Ubincompat5005 \
        -Uversiononly \
        -Dpager='/usr/bin/less -isr' \
        -Dd_gethostent_r_proto -Ud_endhostent_r_proto -Ud_sethostent_r_proto \
        -Ud_endprotoent_r_proto -Ud_setprotoent_r_proto \
        -Ud_endservent_r_proto -Ud_setservent_r_proto \
        -Dscriptdir='%{_bindir}' \
        -Dusesitecustomize

%ifarch sparc64
make
%else
make %{?_smp_mflags}
%endif

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%define build_archlib $RPM_BUILD_ROOT%{archlib}
%define build_privlib $RPM_BUILD_ROOT%{privlib}
%define build_bindir  $RPM_BUILD_ROOT%{_bindir}
%define new_perl LD_PRELOAD="%{build_archlib}/CORE/libperl.so" \\\
        LD_LIBRARY_PATH="%{build_archlib}/CORE" \\\
        PERL5LIB="%{build_archlib}:%{build_privlib}" \\\
        %{build_bindir}/perl

# perl doesn't create the auto subdirectory, but modules put things in it,
# so we need to own it.
mkdir -p -m 755 %{build_archlib}/auto

install -p -m 755 utils/pl2pm %{build_bindir}/pl2pm

for i in asm/termios.h syscall.h syslimits.h syslog.h \
        sys/ioctl.h sys/socket.h sys/time.h wait.h
do
        %{new_perl} %{build_bindir}/h2ph -a -d %{build_archlib} $i || true
done

# vendor directories (in this case for third party rpms)
mkdir -p $RPM_BUILD_ROOT%{archlib}/vendor_perl
mkdir -p $RPM_BUILD_ROOT%{privlib}/vendor_perl

#
# Core modules removal
#
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty | xargs rm -f 

chmod -R u+w $RPM_BUILD_ROOT/*

# miniperl? As an interpreter? How odd. Anyway, a symlink does it:
rm %{build_privlib}/ExtUtils/xsubpp
ln -s ../../../bin/xsubpp %{build_privlib}/ExtUtils/

# Don't need the .packlist
rm %{build_archlib}/.packlist

# Fix some manpages to be UTF-8
pushd $RPM_BUILD_ROOT%{_mandir}/man1/
  for i in perl588delta.1 perldelta.1 ; do
    iconv -f MS-ANSI -t UTF-8 $i --output new-$i
    rm $i
    mv new-$i $i
  done
popd

# compatibility directory: for perl(:MODULE_COMPAT_5.22.0)
mkdir -p $RPM_BUILD_ROOT%{_libdir}/perl5/5.22.0/%{perl_archname}/CORE
ln -s ../../../CORE/libperl.so $RPM_BUILD_ROOT%{_libdir}/perl5/5.22.0/%{perl_archname}/CORE/libperl.so

%clean
rm -rf $RPM_BUILD_ROOT

%check
%ifnarch ppc64 s390 s390x
#ext/threads-shared/t/stress test fails on z10
export PERL_CORE=1
##jrh##FIX THIS##make test
%endif

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc Artistic AUTHORS Copying README Changes
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_bindir}/*
%{privlib}
%{archlib}/*
%{privlib}/vendor_perl
%exclude %{archlib}/vendor_perl

# libs
%exclude %{archlib}/CORE/libperl.so
%exclude %{_libdir}/perl5/5.22.0/%{perl_archname}/CORE/libperl.so

# devel
%exclude %{_bindir}/enc2xs
%exclude %{_mandir}/man1/enc2xs*
%exclude %{privlib}/Encode/
%exclude %{_bindir}/h2xs
%exclude %{_mandir}/man1/h2xs*
%exclude %{_bindir}/libnetcfg
%exclude %{_mandir}/man1/libnetcfg*
%exclude %{_bindir}/perlivp
%exclude %{_mandir}/man1/perlivp*
%exclude %{archlib}/CORE/*.h
%exclude %{_bindir}/xsubpp
%exclude %{_mandir}/man1/xsubpp*

# Archive-Tar
%exclude %{_bindir}/ptar
%exclude %{_bindir}/ptardiff
%exclude %{privlib}/Archive/Tar/
%exclude %{privlib}/Archive/Tar.pm
%exclude %{_mandir}/man1/ptar.1*
%exclude %{_mandir}/man1/ptardiff.1*
%exclude %{_mandir}/man3/Archive::Tar*

# CPAN
%exclude %{_bindir}/cpan
%exclude %{privlib}/CPAN/
%exclude %{privlib}/CPAN.pm
%exclude %{_mandir}/man1/cpan.1*
%exclude %{_mandir}/man3/CPAN.*
%exclude %{_mandir}/man3/CPAN:*

# Parse-CPAN-Meta
%exclude %dir %{privlib}/Parse/
%exclude %dir %{privlib}/Parse/CPAN/
%exclude %{privlib}/Parse/CPAN/Meta.pm
%exclude %{_mandir}/man3/Parse::CPAN::Meta.3*

# Compress::Raw::Bzip2
%exclude %dir %{archlib}/Compress
%exclude %dir %{archlib}/Compress/Raw
%exclude %dir %{archlib}/auto/Compress
%exclude %{archlib}/auto/Compress/Raw/Bzip2
%exclude %{archlib}/Compress/Raw/Bzip2.pm
%exclude %{_mandir}/man3/Compress::Raw::Bzip2*

# Compress::Raw::Zlib
%exclude %dir %{archlib}/Compress
%exclude %dir %{archlib}/Compress/Raw
%exclude %{archlib}/Compress/Raw/Zlib.pm
%exclude %dir %{archlib}/auto/Compress
%exclude %dir %{archlib}/auto/Compress/Raw
%exclude %{archlib}/auto/Compress/Raw/Zlib
%exclude %{_mandir}/man3/Compress::Raw::Zlib*

# Compress::Zlib
%exclude %{privlib}/Compress/Zlib.pm
%exclude %{_mandir}/man3/Compress::Zlib*

# Digest::SHA
%exclude %{_bindir}/shasum
%exclude %{archlib}/Digest/SHA.pm
%exclude %{archlib}/auto/Digest/SHA/
%exclude %{_mandir}/man1/shasum.1*
%exclude %{_mandir}/man3/Digest::SHA.3*

# ExtUtils::CBuilder
%exclude %{privlib}/ExtUtils/CBuilder/
%exclude %{privlib}/ExtUtils/CBuilder.pm
%exclude %{_mandir}/man3/ExtUtils::CBuilder*

# ExtUtils::Embed
%exclude %{privlib}/ExtUtils/Embed.pm
%exclude %{_mandir}/man3/ExtUtils::Embed*

# ExtUtils::MakeMaker
%exclude %{_bindir}/instmodsh
%exclude %{privlib}/ExtUtils/Command/
%exclude %{privlib}/ExtUtils/Install.pm
%exclude %{privlib}/ExtUtils/Installed.pm
%exclude %{privlib}/ExtUtils/Liblist/
%exclude %{privlib}/ExtUtils/Liblist.pm
%exclude %{privlib}/ExtUtils/MakeMaker/
%exclude %{privlib}/ExtUtils/MakeMaker.pm
%exclude %{privlib}/ExtUtils/MANIFEST.SKIP
%exclude %{privlib}/ExtUtils/MM*.pm
%exclude %{privlib}/ExtUtils/MY.pm
%exclude %{privlib}/ExtUtils/Manifest.pm
%exclude %{privlib}/ExtUtils/Mkbootstrap.pm
%exclude %{privlib}/ExtUtils/Mksymlists.pm
%exclude %{privlib}/ExtUtils/Packlist.pm
%exclude %{privlib}/ExtUtils/testlib.pm
%exclude %{_mandir}/man1/instmodsh.1*
%exclude %{_mandir}/man3/ExtUtils::Command::MM*
%exclude %{_mandir}/man3/ExtUtils::Install.3*
%exclude %{_mandir}/man3/ExtUtils::Installed.3*
%exclude %{_mandir}/man3/ExtUtils::Liblist.3*
%exclude %{_mandir}/man3/ExtUtils::MM*
%exclude %{_mandir}/man3/ExtUtils::MY.3*
%exclude %{_mandir}/man3/ExtUtils::MakeMaker*
%exclude %{_mandir}/man3/ExtUtils::Manifest.3*
%exclude %{_mandir}/man3/ExtUtils::Mkbootstrap.3*
%exclude %{_mandir}/man3/ExtUtils::Mksymlists.3*
%exclude %{_mandir}/man3/ExtUtils::Packlist.3*
%exclude %{_mandir}/man3/ExtUtils::testlib.3*

# ExtUtils::ParseXS
%exclude %{privlib}/ExtUtils/ParseXS.pm
%exclude %{privlib}/ExtUtils/xsubpp
%exclude %{_mandir}/man3/ExtUtils::ParseXS.3*

# File::Fetch
%exclude %{privlib}/File/Fetch.pm
%exclude %{_mandir}/man3/File::Fetch.3*

# IO::Compress::Base
%exclude %{privlib}/File/GlobMapper.pm
%exclude %dir %{privlib}/IO/Compress/Adapter/
%exclude %{privlib}/IO/Compress/Base/
%exclude %{privlib}/IO/Compress/Base.pm
%exclude %dir %{privlib}/IO/Uncompress/Adapter/
%exclude %{privlib}/IO/Uncompress/AnyUncompress.pm
%exclude %{privlib}/IO/Uncompress/Base.pm
%exclude %{_mandir}/man3/File::GlobMapper.*
%exclude %{_mandir}/man3/IO::Compress::Base.*
%exclude %{_mandir}/man3/IO::Uncompress::AnyUncompress.*
%exclude %{_mandir}/man3/IO::Uncompress::Base.*

# IO::Compress::Bzip2
%exclude %{privlib}/IO/Compress/Adapter/Bzip2.pm
%exclude %{privlib}/IO/Compress/Bzip2.pm
%exclude %{privlib}/IO/Uncompress/Adapter/Bunzip2.pm
%exclude %{privlib}/IO/Uncompress/Bunzip2.pm
%exclude %{_mandir}/man3/IO::Compress::Bzip2*
%exclude %{_mandir}/man3/IO::Uncompress::Bunzip2*

# IO::Compress::Zlib
%exclude %{privlib}/IO/Compress/Adapter/Deflate.pm
%exclude %{privlib}/IO/Compress/Adapter/Identity.pm
%exclude %{privlib}/IO/Compress/Deflate.pm
%exclude %{privlib}/IO/Compress/Gzip/
%exclude %{privlib}/IO/Compress/Gzip.pm
%exclude %{privlib}/IO/Compress/RawDeflate.pm
%exclude %{privlib}/IO/Compress/Zip/
%exclude %{privlib}/IO/Compress/Zip.pm
%exclude %{privlib}/IO/Uncompress/Adapter/Identity.pm
%exclude %{privlib}/IO/Uncompress/Adapter/Inflate.pm
%exclude %{privlib}/IO/Uncompress/AnyInflate.pm
%exclude %{privlib}/IO/Uncompress/Gunzip.pm
%exclude %{privlib}/IO/Uncompress/Inflate.pm
%exclude %{privlib}/IO/Uncompress/RawInflate.pm
%exclude %{privlib}/IO/Uncompress/Unzip.pm
%exclude %{_mandir}/man3/IO::Compress::Deflate*
%exclude %{_mandir}/man3/IO::Compress::Gzip*
%exclude %{_mandir}/man3/IO::Compress::RawDeflate*
%exclude %{_mandir}/man3/IO::Compress::Zip*
%exclude %{_mandir}/man3/IO::Uncompress::AnyInflate*
%exclude %{_mandir}/man3/IO::Uncompress::Gunzip*
%exclude %{_mandir}/man3/IO::Uncompress::Inflate*
%exclude %{_mandir}/man3/IO::Uncompress::RawInflate*
%exclude %{_mandir}/man3/IO::Uncompress::Unzip*

# IO::Zlib
%exclude %{privlib}/IO/Zlib.pm
%exclude %{_mandir}/man3/IO::Zlib.*

# IPC::Cmd
%exclude %{privlib}/IPC/Cmd.pm
%exclude %{_mandir}/man3/IPC::Cmd.3*

# Locale::Maketext::Simple
%exclude %{privlib}/Locale/Maketext/Simple.pm
%exclude %{_mandir}/man3/Locale::Maketext::Simple.*

# Module-CoreList
%exclude %{_bindir}/corelist
%exclude %{privlib}/Module/CoreList.pm
%exclude %{_mandir}/man1/corelist*
%exclude %{_mandir}/man3/Module::CoreList*

# Module-Load
%exclude %{privlib}/Module/Load.pm
%exclude %{_mandir}/man3/Module::Load.*

# Module-Load-Conditional
%exclude %{privlib}/Module/Load/
%exclude %{_mandir}/man3/Module::Load::Conditional*

# Module-Loaded
%exclude %{privlib}/Module/Loaded.pm
%exclude %{_mandir}/man3/Module::Loaded*

# Params-Check
%exclude %{privlib}/Params/
%exclude %{_mandir}/man3/Params::Check*

# parent
%exclude %{privlib}/parent.pm
%exclude %{_mandir}/man3/parent.3*

# Pod-Escapes
%exclude %{privlib}/Pod/Escapes.pm
%exclude %{_mandir}/man3/Pod::Escapes.*

# Pod-Simple
%exclude %{privlib}/Pod/Simple/
%exclude %{privlib}/Pod/Simple.pm
%exclude %{privlib}/Pod/Simple.pod
%exclude %{_mandir}/man3/Pod::Simple*

# Test::Harness
%exclude %{_bindir}/prove
%exclude %{privlib}/App*
%exclude %{privlib}/TAP*
%exclude %{privlib}/Test/Harness*
%exclude %{_mandir}/man1/prove.1*
%exclude %{_mandir}/man3/App*
%exclude %{_mandir}/man3/TAP*
%exclude %{_mandir}/man3/Test::Harness*

# Test::Simple
%exclude %{privlib}/Test/More*
%exclude %{privlib}/Test/Builder*
%exclude %{privlib}/Test/Simple*
%exclude %{privlib}/Test/Tutorial*
%exclude %{_mandir}/man3/Test::More*
%exclude %{_mandir}/man3/Test::Builder*
%exclude %{_mandir}/man3/Test::Simple*
%exclude %{_mandir}/man3/Test::Tutorial*

# Time::HiRes
%exclude %{archlib}/Time/HiRes.pm
%exclude %{archlib}/auto/Time/HiRes/HiRes.so
%exclude %{_mandir}/man3/Time::HiRes.3*

# Time::Piece
%exclude %{archlib}/Time/Piece.pm
%exclude %{archlib}/Time/Seconds.pm
%exclude %{archlib}/auto/Time/Piece/
%exclude %{_mandir}/man3/Time::Piece.3*
%exclude %{_mandir}/man3/Time::Seconds.3*

# version
%exclude %{privlib}/version.pm
%exclude %{privlib}/version.pod
%exclude %{privlib}/version/
%exclude %{_mandir}/man3/version.3*
%exclude %{_mandir}/man3/version::Internals.3*

%files libs
%defattr(-,root,root)
%{archlib}/CORE/libperl.so
%{_libdir}/perl5/5.22.0/%{perl_archname}/CORE/libperl.so
%dir %{archlib}

%files devel
%defattr(-,root,root,-)
%{_bindir}/enc2xs
%{_mandir}/man1/enc2xs*
%{privlib}/Encode/
%{_bindir}/h2xs
%{_mandir}/man1/h2xs*
%{_bindir}/libnetcfg
%{_mandir}/man1/libnetcfg*
%{_bindir}/perlivp
%{_mandir}/man1/perlivp*
%{archlib}/CORE/*.h
%{_bindir}/xsubpp
%{_mandir}/man1/xsubpp*
#%{_sysconfdir}/rpm/macros.perl

%files Archive-Tar
%defattr(-,root,root,-)
%{_bindir}/ptar
%{_bindir}/ptardiff
%{privlib}/Archive/Tar/ 
%{privlib}/Archive/Tar.pm
%{_mandir}/man1/ptar.1*
%{_mandir}/man1/ptardiff.1*
%{_mandir}/man3/Archive::Tar* 

%files Compress-Raw-Bzip2
%defattr(-,root,root,-)
%dir %{archlib}/Compress
%dir %{archlib}/Compress/Raw
%{archlib}/auto/Compress/Raw/Bzip2
%{archlib}/Compress/Raw/Bzip2.pm
%{_mandir}/man3/Compress::Raw::Bzip2*

%files Compress-Raw-Zlib
%defattr(-,root,root,-)
%dir %{archlib}/Compress
%dir %{archlib}/Compress/Raw
%{archlib}/Compress/Raw/Zlib.pm
%dir %{archlib}/auto/Compress
%dir %{archlib}/auto/Compress/Raw
%{archlib}/auto/Compress/Raw/Zlib
%{_mandir}/man3/Compress::Raw::Zlib*

%files Compress-Zlib
%defattr(-,root,root,-)
%{privlib}/Compress/Zlib.pm
%{_mandir}/man3/Compress::Zlib*

%files CPAN
%defattr(-,root,root,-)
%{_bindir}/cpan
%{privlib}/CPAN/
%{privlib}/CPAN.pm
%{_mandir}/man1/cpan.1*
%{_mandir}/man3/CPAN.*
%{_mandir}/man3/CPAN:*

%files Digest-SHA
%defattr(-,root,root,-)
%{_bindir}/shasum
%dir %{archlib}/Digest/
%{archlib}/Digest/SHA.pm
%{archlib}/auto/Digest/SHA/
%{_mandir}/man1/shasum.1*
%{_mandir}/man3/Digest::SHA.3*

%files ExtUtils-CBuilder
%defattr(-,root,root,-)
%{privlib}/ExtUtils/CBuilder/
%{privlib}/ExtUtils/CBuilder.pm
%{_mandir}/man3/ExtUtils::CBuilder*

%files ExtUtils-Embed
%defattr(-,root,root,-)
%{privlib}/ExtUtils/Embed.pm
%{_mandir}/man3/ExtUtils::Embed*

%files ExtUtils-MakeMaker
%defattr(-,root,root,-)
%{_bindir}/instmodsh
%{privlib}/ExtUtils/Command/
%{privlib}/ExtUtils/Install.pm
%{privlib}/ExtUtils/Installed.pm
%{privlib}/ExtUtils/Liblist/
%{privlib}/ExtUtils/Liblist.pm
%{privlib}/ExtUtils/MakeMaker/
%{privlib}/ExtUtils/MakeMaker.pm
%{privlib}/ExtUtils/MANIFEST.SKIP
%{privlib}/ExtUtils/MM*.pm
%{privlib}/ExtUtils/MY.pm
%{privlib}/ExtUtils/Manifest.pm
%{privlib}/ExtUtils/Mkbootstrap.pm
%{privlib}/ExtUtils/Mksymlists.pm
%{privlib}/ExtUtils/Packlist.pm
%{privlib}/ExtUtils/testlib.pm
%{_mandir}/man1/instmodsh.1*
%{_mandir}/man3/ExtUtils::Command::MM*
%{_mandir}/man3/ExtUtils::Install.3*
%{_mandir}/man3/ExtUtils::Installed.3*
%{_mandir}/man3/ExtUtils::Liblist.3*
%{_mandir}/man3/ExtUtils::MM*
%{_mandir}/man3/ExtUtils::MY.3*
%{_mandir}/man3/ExtUtils::MakeMaker*
%{_mandir}/man3/ExtUtils::Manifest.3*
%{_mandir}/man3/ExtUtils::Mkbootstrap.3*
%{_mandir}/man3/ExtUtils::Mksymlists.3*
%{_mandir}/man3/ExtUtils::Packlist.3*
%{_mandir}/man3/ExtUtils::testlib.3*

%files ExtUtils-ParseXS
%defattr(-,root,root,-)
%{privlib}/ExtUtils/ParseXS.pm
%{privlib}/ExtUtils/xsubpp
%{_mandir}/man3/ExtUtils::ParseXS.3*

%files File-Fetch
%defattr(-,root,root,-)
%{privlib}/File/Fetch.pm
%{_mandir}/man3/File::Fetch.3*

%files IO-Compress-Base
%defattr(-,root,root,-)
%{privlib}/File/GlobMapper.pm
%dir %{privlib}/IO/Compress/Adapter/
%{privlib}/IO/Compress/Base/
%{privlib}/IO/Compress/Base.pm
%dir %{privlib}/IO/Uncompress/Adapter/
%{privlib}/IO/Uncompress/AnyUncompress.pm
%{privlib}/IO/Uncompress/Base.pm
%{_mandir}/man3/File::GlobMapper.*
%{_mandir}/man3/IO::Compress::Base.*
%{_mandir}/man3/IO::Uncompress::AnyUncompress.*
%{_mandir}/man3/IO::Uncompress::Base.*

%files IO-Compress-Bzip2
%defattr(-,root,root,-)
%{privlib}/IO/Compress/Adapter/Bzip2.pm
%{privlib}/IO/Compress/Bzip2.pm
%{privlib}/IO/Uncompress/Adapter/Bunzip2.pm
%{privlib}/IO/Uncompress/Bunzip2.pm
%{_mandir}/man3/IO::Compress::Bzip2*
%{_mandir}/man3/IO::Uncompress::Bunzip2*

%files IO-Compress-Zlib
%defattr(-,root,root,-)
%{privlib}/IO/Compress/Adapter/Deflate.pm
%{privlib}/IO/Compress/Adapter/Identity.pm
%{privlib}/IO/Compress/Deflate.pm
%{privlib}/IO/Compress/Gzip/
%{privlib}/IO/Compress/Gzip.pm
%{privlib}/IO/Compress/RawDeflate.pm
%{privlib}/IO/Compress/Zip/
%{privlib}/IO/Compress/Zip.pm
%{privlib}/IO/Uncompress/Adapter/Identity.pm
%{privlib}/IO/Uncompress/Adapter/Inflate.pm
%{privlib}/IO/Uncompress/AnyInflate.pm
%{privlib}/IO/Uncompress/Gunzip.pm
%{privlib}/IO/Uncompress/Inflate.pm
%{privlib}/IO/Uncompress/RawInflate.pm
%{privlib}/IO/Uncompress/Unzip.pm
%{_mandir}/man3/IO::Compress::Deflate*
%{_mandir}/man3/IO::Compress::Gzip*
%{_mandir}/man3/IO::Compress::RawDeflate*
%{_mandir}/man3/IO::Compress::Zip*
%{_mandir}/man3/IO::Uncompress::AnyInflate*
%{_mandir}/man3/IO::Uncompress::Gunzip*
%{_mandir}/man3/IO::Uncompress::Inflate*
%{_mandir}/man3/IO::Uncompress::RawInflate*
%{_mandir}/man3/IO::Uncompress::Unzip*

%files IO-Zlib
%defattr(-,root,root,-)
%{privlib}/IO/Zlib.pm
%{_mandir}/man3/IO::Zlib.*

%files IPC-Cmd
%defattr(-,root,root,-)
%{privlib}/IPC/Cmd.pm
%{_mandir}/man3/IPC::Cmd.3*

%files Locale-Maketext-Simple
%defattr(-,root,root,-)
%{privlib}/Locale/Maketext/Simple.pm
%{_mandir}/man3/Locale::Maketext::Simple.*

%files Module-CoreList
%defattr(-,root,root,-)
%{_bindir}/corelist
%{privlib}/Module/CoreList.pm
%{_mandir}/man1/corelist*
%{_mandir}/man3/Module::CoreList*

%files Module-Load
%defattr(-,root,root,-)
%{privlib}/Module/Load.pm
%{_mandir}/man3/Module::Load.*

%files Module-Load-Conditional
%defattr(-,root,root,-)
%{privlib}/Module/Load/
%{_mandir}/man3/Module::Load::Conditional* 

%files Module-Loaded
%defattr(-,root,root,-)
%dir %{privlib}/Module/
%{privlib}/Module/Loaded.pm
%{_mandir}/man3/Module::Loaded*

%files Params-Check
%defattr(-,root,root,-)
%{privlib}/Params/
%{_mandir}/man3/Params::Check*

%files Parse-CPAN-Meta
%defattr(-,root,root,-)
%dir %{privlib}/Parse/
%dir %{privlib}/Parse/CPAN/
%{privlib}/Parse/CPAN/Meta.pm
%{_mandir}/man3/Parse::CPAN::Meta.3*

%files Pod-Escapes
%defattr(-,root,root,-)
%{privlib}/Pod/Escapes.pm
%{_mandir}/man3/Pod::Escapes.*

%files Pod-Simple
%defattr(-,root,root,-)
%{privlib}/Pod/Simple/ 
%{privlib}/Pod/Simple.pm
%{privlib}/Pod/Simple.pod
%{_mandir}/man3/Pod::Simple*

%files Test-Harness
%defattr(-,root,root,-)
%{_bindir}/prove
%{privlib}/App*
%{privlib}/TAP*
%{privlib}/Test/Harness*
%{_mandir}/man1/prove.1*
%{_mandir}/man3/App*
%{_mandir}/man3/TAP*
%{_mandir}/man3/Test::Harness*

%files Test-Simple
%defattr(-,root,root,-)
%{privlib}/Test/More*
%{privlib}/Test/Builder*
%{privlib}/Test/Simple*
%{privlib}/Test/Tutorial*
%{_mandir}/man3/Test::More*
%{_mandir}/man3/Test::Builder*
%{_mandir}/man3/Test::Simple*
%{_mandir}/man3/Test::Tutorial*

%files Time-HiRes
%defattr(-,root,root,-)
%{archlib}/Time/HiRes.pm
%{archlib}/auto/Time/HiRes/HiRes.so
%{_mandir}/man3/Time::HiRes.3*

%files Time-Piece
%defattr(-,root,root,-)
%{archlib}/Time/Piece.pm 
%{archlib}/Time/Seconds.pm
%{archlib}/auto/Time/Piece/        
%{_mandir}/man3/Time::Piece.3*
%{_mandir}/man3/Time::Seconds.3*

%files parent 
%defattr(-,root,root,-)
%{privlib}/parent.pm
%{_mandir}/man3/parent.3*

%files version
%defattr(-,root,root,-)
%{privlib}/version.pm
%{privlib}/version.pod
%{privlib}/version/
%{_mandir}/man3/version.3*
%{_mandir}/man3/version::Internals.3*

%files core
# Nothing. Nada. Zilch. Zarro. Uh uh. Nope. Sorry.

%changelog
* Thu Jun 11 2015 James Hunt <jhunt@3c.com> - 4:5.22.0-1
- Package 5.22 for CentOS 6
