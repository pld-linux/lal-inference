# TODO: MPI
Summary:	LAL routines for Bayesian inference data analysis
Summary(pl.UTF-8):	Procedury LAL do analizy danych wywodów bayesowskich
Name:		lal-inference
Version:	4.1.1
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://software.igwn.org/lscsoft/source/lalsuite/lalinference-%{version}.tar.xz
# Source0-md5:	9391ce2650fc47fcb34154d398b32bac
Patch0:		lalinference-env.patch
Patch1:		lalinference-format.patch
URL:		https://wiki.ligo.org/Computing/LALSuite
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gsl-devel >= 1.15
BuildRequires:	help2man
BuildRequires:	lal-devel >= 7.2.2
BuildRequires:	lal-burst-devel >= 1.6.0
BuildRequires:	lal-frame-devel >= 2.0.0
BuildRequires:	lal-inspiral-devel >= 3.0.0
BuildRequires:	lal-metaio-devel >= 3.0.0
BuildRequires:	lal-simulation-devel >= 4.0.0
BuildRequires:	libgomp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	octave-devel >= 1:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-numpy-devel >= 1:1.7
BuildRequires:	sed >= 4.0
BuildRequires:	swig >= 4.1.0
BuildRequires:	swig-python >= 3.0.11
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gsl >= 1.15
Requires:	lal >= 7.2.2
Requires:	lal-burst >= 1.6.0
Requires:	lal-frame >= 2.0.0
Requires:	lal-inspiral >= 3.0.0
Requires:	lal-metaio >= 3.0.0
Requires:	lal-simulation >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LAL routines for Bayesian inference data analysis.

%description -l pl.UTF-8
Procedury LAL do analizy danych wywodów bayesowskich.

%package devel
Summary:	Header files for lal-inference library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lal-inference
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gsl-devel >= 1.15
Requires:	lal-devel >= 7.2.2
Requires:	lal-burst-devel >= 1.6.0
Requires:	lal-frame-devel >= 2.0.0
Requires:	lal-inspiral-devel >= 3.0.0
Requires:	lal-metaio-devel >= 3.0.0
Requires:	lal-simulation-devel >= 4.0.0

%description devel
Header files for lal-inference library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lal-inference.

%package static
Summary:	Static lal-inference library
Summary(pl.UTF-8):	Statyczna biblioteka lal-inference
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lal-inference library.

%description static -l pl.UTF-8
Statyczna biblioteka lal-inference.

%package -n octave-lalinference
Summary:	Octave interface for LAL Inference
Summary(pl.UTF-8):	Interfejs Octave do biblioteki LAL Inference
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}
Requires:	octave-lal >= 7.2.2

%description -n octave-lalinference
Octave interface for LAL Inference.

%description -n octave-lalinference -l pl.UTF-8
Interfejs Octave do biblioteki LAL Inference.

%package -n python3-lalinference
Summary:	Python bindings for LAL Inference
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki LAL Inference
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-lal >= 7.2.2
Requires:	python3-lalburst >= 1.6.0
Requires:	python3-lalmetaio >= 3.0.0
Requires:	python3-lalinspieral >= 3.0.0
Requires:	python3-lalsimulation >= 4.0.0
Requires:	python3-ligo-lw >= 1.7.0
Requires:	python3-ligo-segments
Requires:	python3-lscsoft-glue >= 1.54.1
Requires:	python3-matplotlib >= 1.2.0
Requires:	python3-modules >= 1:3.5
Requires:	python3-numpy >= 1:1.7
Requires:	python3-six
Requires:	python3-scipy >= 0.9.0
# TODO: healpy>=1.9.1 astropy>=1.1.1 gwdatafind gwpy h5py

%description -n python3-lalinference
Python bindings for LAL Inference.

%description -n python3-lalinference -l pl.UTF-8
Wiązania Pythona do biblioteki LAL Inference.

%prep
%setup -q -n lalinference-%{version}
%patch0 -p1
%patch1 -p1

%{__sed} -i -e '1s,/usr/bin/env bash,/bin/bash,' bin/lalinference_mpi_wrapper

%build
%{__libtoolize}
%{__aclocal} -I gnuscripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-swig

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/lalinference/_bayespputils.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblalinference.la

install -d $RPM_BUILD_ROOT/etc/shrc.d
%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/*sh $RPM_BUILD_ROOT/etc/shrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lalinference_bench
%attr(755,root,root) %{_bindir}/lalinference_burst
%attr(755,root,root) %{_bindir}/lalinference_datadump
%attr(755,root,root) %{_bindir}/lalinference_injectedlike
%attr(755,root,root) %{_bindir}/lalinference_mpi_wrapper
%attr(755,root,root) %{_bindir}/lalinference_nest
%attr(755,root,root) %{_bindir}/lalinference_version
%attr(755,root,root) %{_libdir}/liblalinference.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblalinference.so.23
/etc/shrc.d/lalinference-user-env.csh
/etc/shrc.d/lalinference-user-env.fish
/etc/shrc.d/lalinference-user-env.sh
%{_datadir}/lalinference
%{_mandir}/man1/lalinference_bench.1*
%{_mandir}/man1/lalinference_burst.1*
%{_mandir}/man1/lalinference_datadump.1*
%{_mandir}/man1/lalinference_injectedlike.1*
%{_mandir}/man1/lalinference_nest.1*
%{_mandir}/man1/lalinference_version.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblalinference.so
%{_includedir}/lal/LALInference*.h
%{_includedir}/lal/SWIGLALInferenceTest.h
%{_includedir}/lal/SWIGLALInference*.i
%{_includedir}/lal/cubic_interp.h
%{_includedir}/lal/distance_integrator.h
%{_includedir}/lal/swiglalinference.i
%{_pkgconfigdir}/lalinference.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblalinference.a

%files -n octave-lalinference
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/octave/*/site/oct/*/lalinference.oct

%files -n python3-lalinference
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cbcBayes*
%attr(755,root,root) %{_bindir}/imrtgr_imr_consistency_test
%attr(755,root,root) %{_bindir}/lalinference_burst_pp_pipe
%attr(755,root,root) %{_bindir}/lalinference_coherence_test
%attr(755,root,root) %{_bindir}/lalinference_compute_roq_weights
%attr(755,root,root) %{_bindir}/lalinference_cpnest
%attr(755,root,root) %{_bindir}/lalinference_evolve_spins_and_append_samples
%attr(755,root,root) %{_bindir}/lalinference_merge_posteriors
%attr(755,root,root) %{_bindir}/lalinference_multi_pipe
%attr(755,root,root) %{_bindir}/lalinference_nest2pos
%attr(755,root,root) %{_bindir}/lalinference_pipe
%attr(755,root,root) %{_bindir}/lalinference_pp_pipe
%attr(755,root,root) %{_bindir}/lalinference_review_test
%dir %{py3_sitedir}/lalinference
%attr(755,root,root) %{py3_sitedir}/lalinference/_bayespputils.so
%attr(755,root,root) %{py3_sitedir}/lalinference/_lalinference.so
%{py3_sitedir}/lalinference/*.py
%{py3_sitedir}/lalinference/__pycache__
%dir %{py3_sitedir}/lalinference/bayestar
%{py3_sitedir}/lalinference/bayestar/*.py
%{py3_sitedir}/lalinference/bayestar/__pycache__
%dir %{py3_sitedir}/lalinference/imrtgr
%{py3_sitedir}/lalinference/imrtgr/*.py
%{py3_sitedir}/lalinference/imrtgr/__pycache__
%dir %{py3_sitedir}/lalinference/io
%{py3_sitedir}/lalinference/io/*.py
%{py3_sitedir}/lalinference/io/__pycache__
%dir %{py3_sitedir}/lalinference/plot
%{py3_sitedir}/lalinference/plot/*.py
%{py3_sitedir}/lalinference/plot/__pycache__
%dir %{py3_sitedir}/lalinference/tiger
%{py3_sitedir}/lalinference/tiger/*.py
%{py3_sitedir}/lalinference/tiger/__pycache__
%{_mandir}/man1/cbcBayes*.1*
%{_mandir}/man1/imrtgr_imr_consistency_test.1*
%{_mandir}/man1/lalinference_burst_pp_pipe.1*
%{_mandir}/man1/lalinference_coherence_test.1*
%{_mandir}/man1/lalinference_compute_roq_weights.1*
%{_mandir}/man1/lalinference_cpnest.1*
%{_mandir}/man1/lalinference_evolve_spins_and_append_samples.1*
%{_mandir}/man1/lalinference_merge_posteriors.1*
%{_mandir}/man1/lalinference_multi_pipe.1*
%{_mandir}/man1/lalinference_nest2pos.1*
%{_mandir}/man1/lalinference_pipe.1*
%{_mandir}/man1/lalinference_pp_pipe.1*
%{_mandir}/man1/lalinference_review_test.1*
