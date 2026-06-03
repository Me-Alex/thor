export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/api/health') return Response.json({ ok: true, service: 'Thor' });
    if (url.pathname === '/api/listings') {
      const upstream = env.API_BASE_URL || 'http://localhost:8000';
      const target = new URL('/listings' + url.search, upstream);
      const res = await fetch(target, request);
      return new Response(await res.text(), { status: res.status, headers: { 'content-type': 'application/json' } });
    }
    return env.ASSETS.fetch(request);
  }
};
