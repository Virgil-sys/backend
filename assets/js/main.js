// Smooth scroll for in-page anchors
document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;
    const id = a.getAttribute('href');
    const target = document.querySelector(id);
    if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
});

// If the page loads with a hash, smooth-scroll to it once DOM is ready
window.addEventListener('DOMContentLoaded', () => {
    if (location.hash) {
        const el = document.querySelector(location.hash);
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
});

// Sticky nav shadow
(function(){
    const nav = document.querySelector('nav');
    const onScroll = () => { if (nav) nav.classList.toggle('shadow-md', window.scrollY > 4); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
})();

// Reveal on scroll
(function(){
    const els = document.querySelectorAll('.activity-card, .transport-tier');
    if (!els.length) return;
    const io = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                io.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12 });
    els.forEach((el) => { el.classList.add('reveal'); io.observe(el); });
})();

// Modal helper
function setupModal(openBtnId, modalId, closeIds = []) {
    const openBtn = document.getElementById(openBtnId);
    const modal = document.getElementById(modalId);
    if (!modal) return;
    const closeButtons = closeIds.map((id) => document.getElementById(id)).filter(Boolean);
    const show = () => { modal.classList.remove('hidden'); modal.classList.add('flex'); document.body.style.overflow = 'hidden'; };
    const hide = () => { modal.classList.add('hidden'); modal.classList.remove('flex'); document.body.style.overflow = ''; };
    if (openBtn) openBtn.addEventListener('click', show);
    closeButtons.forEach((btn) => btn.addEventListener('click', hide));
    modal.addEventListener('click', (e) => { if (e.target === modal) hide(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') hide(); });
}

// Wire up known modals if present
setupModal('open-explore-modal', 'explore-modal', ['close-explore-modal']);
setupModal('open-packages-modal', 'packages-modal', ['close-packages-modal']);
setupModal('open-history-modal', 'history-modal', ['close-history-modal']);

// Viewpoint image slider (if present)
(function(){
    const slider = document.getElementById('viewpoint-slider');
    if (!slider) return;
    const slides = Array.from(slider.querySelectorAll('.vp-slide'));
    const indicators = Array.from(document.querySelectorAll('#vp-indicators button'));
    const prevBtn = document.getElementById('vp-prev');
    const nextBtn = document.getElementById('vp-next');
    let current = 0;
    function show(i){
        slides.forEach((s, idx) => {
            s.classList.toggle('opacity-100', idx === i);
            s.classList.toggle('opacity-0', idx !== i);
        });
        indicators.forEach((ind, idx) => {
            ind.classList.toggle('bg-white', idx === i);
            ind.classList.toggle('bg-white/50', idx !== i);
        });
        current = i;
    }
    indicators.forEach((btn, i) => btn && btn.addEventListener('click', () => show(i)));
    if (prevBtn) prevBtn.addEventListener('click', () => show((current - 1 + slides.length) % slides.length));
    if (nextBtn) nextBtn.addEventListener('click', () => show((current + 1) % slides.length));
    let auto = setInterval(() => show((current + 1) % slides.length), 5000);
    slider.addEventListener('mouseenter', () => clearInterval(auto));
    slider.addEventListener('mouseleave', () => auto = setInterval(() => show((current + 1) % slides.length), 5000));
    show(0);
})();

// Hero Video Rotator (supports up to 5 videos, 4s interval, crossfade)
(function(){
    const wrapper = document.querySelector('.hero-video-wrapper');
    if (!wrapper) return;

    const videoA = wrapper.querySelector('#hero-video-a');
    const videoB = wrapper.querySelector('#hero-video-b');
    if (!videoA || !videoB) return;

    // Edit or extend this list as new videos are added
    const playlist = [
        'videos/video1.mp4',
        'videos/video2.mp4',
        'videos/video3.mp4',
        'videos/video4.mp4',
        'videos/video5.mp4'
    ];

    let currentIndex = 0;
    let showingA = true;
    const INTERVAL_MS = 4000;

    function setSource(videoEl, src) {
        return new Promise((resolve) => {
            const onCanPlay = () => { videoEl.removeEventListener('canplay', onCanPlay); resolve(true); };
            const onError = () => { videoEl.removeEventListener('error', onError); resolve(false); };
            videoEl.addEventListener('canplay', onCanPlay, { once: true });
            videoEl.addEventListener('error', onError, { once: true });
            videoEl.src = src;
            videoEl.load();
        });
    }

    function nextIndex(i){ return (i + 1) % playlist.length; }

    async function rotate() {
        const next = nextIndex(currentIndex);
        const nextSrc = playlist[next];
        const incoming = showingA ? videoB : videoA;
        const outgoing = showingA ? videoA : videoB;

        const ok = await setSource(incoming, nextSrc);
        if (!ok) {
            // Skip missing/broken video
            currentIndex = next;
            setTimeout(rotate, INTERVAL_MS);
            return;
        }

        try { await incoming.play(); } catch(_) {}
        incoming.classList.add('active');
        outgoing.classList.remove('active');

        currentIndex = next;
        showingA = !showingA;
        setTimeout(rotate, INTERVAL_MS);
    }

    // Initialize with first available video
    (async function init(){
        const ok = await setSource(videoA, playlist[currentIndex]);
        if (ok) { try { await videoA.play(); } catch(_) {} videoA.classList.add('active'); }
        setTimeout(rotate, INTERVAL_MS);
    })();
})();

// Pause hero videos when tab hidden
document.addEventListener('visibilitychange', () => {
    const vids = document.querySelectorAll('.hero-video');
    vids.forEach(v => { if (document.hidden) v.pause(); else v.play().catch(()=>{}); });
});


