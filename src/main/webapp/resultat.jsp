<jsp:include page="header.jsp"/>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
  String[] result = (String[]) request.getAttribute("result");
%>

<header class="pt-5">
  <div class="container pt-4 pt-xl-5">
    <div class="row pt-5">
      <div class="col-md-8 text-center text-md-start mx-auto">
        <div class="text-center">
          <h1 class="display-4 fw-bold mb-5">Resultat de la<span class="underline"> prediction</span>.</h1>
          <%for(String line : result) { %>
          <p><%=line%></p>
          <% } %>

        </div>
      </div>
      <div class="col-12 col-lg-10 mx-auto">
        <div class="text-center position-relative"><img class="img-fluid" src="${pageContext.request.contextPath}/static/assets/img/illustrations/meeting.svg" style="width: 800px;"></div>
      </div>
    </div>
  </div>
</header>
<jsp:include page="footer.jsp"/>
