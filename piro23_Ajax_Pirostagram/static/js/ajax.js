// CSRF Setup for Axios
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

// Like button (no changes here)
const onClickLike = async (id, type) => {
    const url = typeof likeAjaxUrl !== 'undefined' ? likeAjaxUrl : '/like_ajax/';
    const { data } = await axios.post(url, { id, type });
    likeHandleResponse(data.id, data.type, data.like_count, data.liked);
};

const likeHandleResponse = (id, type, likeCount, liked) => {
    const likeSpan = document.querySelector(`.post-id-${id}.post__${type}`);
    const likeBtn = document.querySelector(`.like-btn[data-post-id="${id}"]`);
    if (likeSpan && likeBtn) {
        likeSpan.innerHTML = `${likeCount} likes`;
        likeBtn.innerHTML = liked ? '💙' : '🤍';
    }
};

document.addEventListener("DOMContentLoaded", () => {
    document.addEventListener("click", async (e) => {
        const target = e.target.closest(".delete-comment-btn");
        if (!target) return;

        const commentId = target.dataset.commentId;
        if (!commentId) return; 

        const confirmDelete = confirm("정말 삭제하시겠습니까?");
        if (!confirmDelete) return;

        try {
            const res = await axios.post(`/delete_comment_ajax/${commentId}/`);
            if (res.data.deleted) {
                const commentEl = document.getElementById(`comment-${commentId}`);
                if (commentEl) commentEl.remove();
            }
        } catch (err) {
            console.error("댓글 삭제 오류:", err);
        }
    });

    document.querySelectorAll(".comment-form").forEach(form => {
        form.addEventListener("submit", async (e) => {
            e.preventDefault();

            const postId = form.dataset.postId;
            const input = form.querySelector("input[name='content']");
            const content = input.value.trim();
            if (!content) return;

            try {
                const res = await axios.post(`/add_comment_ajax/${postId}/`, { content });
                const data = res.data;

                if (!data.id) {
                    console.error("댓글 ID 없음!");
                    return;
                }

                const commentSection = document.getElementById(`comments-${postId}`);
                const newComment = document.createElement("div");
                newComment.id = `comment-${data.id}`;
                newComment.classList.add("comment-item");

                newComment.innerHTML = `
                    <strong>${data.username}</strong> ${data.content}
                    <button type="button" class="delete-comment-btn" data-comment-id="${data.id}">🗑️</button>
                `;

                commentSection.appendChild(newComment);
                input.value = "";
            } catch (error) {
                console.error("Error adding comment:", error);
            }
        });
    });
});



//Add_Comment
// document.addEventListener("DOMContentLoaded", () => {
//     document.querySelectorAll(".comment-form").forEach(form => {
//         form.addEventListener("submit", async (e) => {
//             e.preventDefault();

//             const postId = form.dataset.postId;
//             const input = form.querySelector("input[name='content']");
//             const content = input.value;

//             if (!content.trim()) return;

//             try {
//                 const res = await axios.post(`/add_comment_ajax/${postId}/`, { content });
//                 const data = res.data;

//                 const commentSection = document.getElementById(`comments-${postId}`);
//                 const newComment = document.createElement("div");
//                 newComment.innerHTML = `<strong>${data.username}</strong> ${data.content}`;
//                 commentSection.appendChild(newComment);

//                 input.value = "";
//             } catch (error) {
//                 console.error("Error adding comment:", error);
//             }
//         });
//     });
// });