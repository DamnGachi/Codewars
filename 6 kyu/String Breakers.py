def string_breakers(n, st):
    st=''.join(st.split())
    return '\n'.join([st[i:i + n] for i in range(0, len(st), n)])
