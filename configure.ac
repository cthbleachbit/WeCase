#AC_CONFIG_MACRO_DIRS([m4])
m4_include([m4/AC_PYTHON_MODULE.m4])
m4_include([m4/acx.m4])

AC_INIT([WeCase], [0.06-beta4])

AM_INIT_AUTOMAKE
AM_PATH_PYTHON([3.2],, AC_MSG_ERROR(Could not find Python >= 3.2.))

AC_PYTHON_MODULE([PyQt4])
if test $HAVE_PYMOD_PYQT4 = "no"; then
    AC_MSG_ERROR(Could not find Python module PyQt4.)
fi

AC_PYTHON_MODULE([weibo3])
if test $HAVE_PYMOD_WEIBO3 = "no"; then
    AC_MSG_ERROR(Could not find Python module weibo3.)
fi

AC_PYTHON_MODULE([notify2])
if test $HAVE_PYMOD_NOTIFY2 = "no"; then
    AC_MSG_WARN(Could not find Python module notify2, notification is unavaliable.)
fi

ACX_PKGPROVIDER([WeCase Developers])
ACX_BUGURL([http://bugs.wecase.org/])

AC_CONFIG_FILES([Makefile src/Makefile locale/Makefile res/Makefile])

AC_OUTPUT
