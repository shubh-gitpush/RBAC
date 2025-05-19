<h1 align="center">📰 Django Role-Based Blogging Website</h1>

<p align="center">
  <strong>A secure, scalable, and responsive blogging platform with role-based user management</strong>
</p>

<hr>

<h2>🚀 Features</h2>

<ul>
  <li>✅ Create and manage blog posts</li>
  <li>✅ Login & Logout system using Django Authentication</li>
  <li>✅ Role-based access control (<code>Superuser</code>, <code>Admin</code>, <code>Moderator</code>, <code>User</code>)</li>
  <li>✅ Add/Edit/Delete comments with permission control</li>
  <li>✅ Responsive UI using Bootstrap</li>
  <li>✅ Secure access via <code>@login_required</code> and <code>@permission_required</code> decorators</li>
  <li>✅ Admin panel for full backend management</li>
</ul>

<hr>

<h2>🔐 Role-Based Access System</h2>

<table>
  <thead>
    <tr>
      <th>Role</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Superuser</strong></td>
      <td>Full control. Can manage Admins, Moderators, Users, and all blog content.</td>
    </tr>
    <tr>
      <td><strong>Admin</strong></td>
      <td>Access granted by Superuser. Can manage Moderators and moderate content.</td>
    </tr>
    <tr>
      <td><strong>Moderator</strong></td>
      <td>Granted by Admin/Superuser. Can view/add comments via admin panel if permitted.</td>
    </tr>
    <tr>
      <td><strong>User</strong></td>
      <td>Default role. Can view blogs and post comments (if allowed).</td>
    </tr>
  </tbody>
</table>

<p>🔒 <strong>Note:</strong> Moderators cannot add comments directly from the UI unless explicitly given permission through the admin panel.</p>

<hr>

<h2>🛠 How to Run the Project</h2>

<h3>📦 Backend (Django)</h3>

<ol>
  <li><strong>Clone the Repository</strong></li>

  <pre><code>git clone https://github.com/yourusername/blog.git
cd blog/blog</code></pre>

  <li><strong>Create a Virtual Environment</strong></li>

  <pre><code>python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate</code></pre>

  <li><strong>Install Dependencies</strong></li>

  <pre><code>pip install -r requirements.txt</code></pre>

  <li><strong>Apply Migrations</strong></li>

  <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>

  <li><strong>Create a Superuser</strong></li>

  <pre><code>python manage.py createsuperuser</code></pre>

  <li><strong>Run the Server</strong></li>

  <pre><code>python manage.py runserver</code></pre>

  <p>🔗 Visit: <a href="http://127.0.0.1:8000" target="_blank">http://127.0.0.1:8000</a></p>
</ol>



<h2>📬 Contact</h2>

<p>
  📧 Email: <a href="mailto:shubhrai598@gmail.com">shubhrai598@gmail.com</a><br>
  💻 GitHub: <a href="https://github.com/shubh-gitpush" target="_blank">github.com/shubh-gitpush</a>
</p>
