document.addEventListener('DOMContentLoaded', () => {
    // Thuật toán mồi Vercel Ready
    console.log("Antigravity Hub System (SSG Generated) Initialized! 100% Code is Functional.");
});

function switchTab(tabId, element) {
    // 1. Ẩn toàn bộ nội dung Tab
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => {
        tab.classList.remove('active-tab');
    });

    // 2. Tẩy màu Active ở toàn bộ Cột Menu (Sidebar)
    const links = document.querySelectorAll('.nav-links li');
    links.forEach(li => {
        li.classList.remove('active');
    });

    // 3. Hiển thị Nội dung Tab được click
    document.getElementById(tabId).classList.add('active-tab');
    element.classList.add('active');
}
