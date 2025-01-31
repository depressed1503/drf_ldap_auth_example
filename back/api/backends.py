from django_auth_ldap.backend import LDAPBackend

class CustomLDAPBackend(LDAPBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try authenticating as a regular user under ou=users
        user = super().authenticate(request, username, password, **kwargs)
        if user:
            return user

        # If regular user authentication fails, try authenticating as admin
        try:
            admin_dn = f"cn={username},dc=example,dc=org"
            print(admin_dn)
            self._get_or_create_user(admin_dn, username, password)
            return super().authenticate(request, username, password, **kwargs)
        except Exception:
            return None
