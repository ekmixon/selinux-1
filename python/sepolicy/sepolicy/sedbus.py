import sys
import dbus
import dbus.service
import dbus.mainloop.glib


class SELinuxDBus (object):

    def __init__(self):
        self.bus = dbus.SystemBus()
        self.dbus_object = self.bus.get_object("org.selinux", "/org/selinux/object")

    def semanage(self, buf):
        return self.dbus_object.semanage(buf, dbus_interface="org.selinux")

    def restorecon(self, path):
        return self.dbus_object.restorecon(path, dbus_interface="org.selinux")

    def setenforce(self, value):
        return self.dbus_object.setenforce(value, dbus_interface="org.selinux")

    def customized(self):
        return self.dbus_object.customized(dbus_interface="org.selinux")

    def semodule_list(self):
        return self.dbus_object.semodule_list(dbus_interface="org.selinux")

    def relabel_on_boot(self, value):
        return self.dbus_object.relabel_on_boot(value, dbus_interface="org.selinux")

    def change_default_mode(self, value):
        return self.dbus_object.change_default_mode(
            value, dbus_interface="org.selinux"
        )

    def change_default_policy(self, value):
        return self.dbus_object.change_default_policy(
            value, dbus_interface="org.selinux"
        )

if __name__ == "__main__":
    try:
        dbus_proxy = SELinuxDBus()
        resp = dbus_proxy.setenforce(int(sys.argv[1]))
        print(resp)
    except dbus.DBusException as e:
        print(e)
