# Generated from rubocop-1.37.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rubocop

Name: rubygem-%{gem_name}
Version: 1.37.0
Release: 1%{?dist}
Summary: Automatic Ruby code style checking tool
License: MIT
URL: https://github.com/rubocop/rubocop
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.6.0
BuildArch: noarch

%description
RuboCop is a Ruby code style checking and code formatting tool.
It aims to enforce the community-driven Ruby Style Guide.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%{_bindir}/rubocop
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/assets
%{gem_instdir}/config
%{gem_instdir}/exe
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Oct 20 2022 Pavel Valena <pvalena@redhat.com> - 1.37.0-1
- Initial package
