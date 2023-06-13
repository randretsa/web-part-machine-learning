<jsp:include page="header.jsp"/>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>


<section class="py-5 mt-5">
    <div class="container py-5">
        <div class="row">
            <div class="col-md-8 col-xl-6 text-center mx-auto">
                <h2 class="display-6 fw-bold mb-4">Nouvelle<span class="underline"> prediction</span>?</h2>
                <p class="text-muted">inserer le code binaire ici.</p>
            </div>
        </div>
        <div class="row d-flex justify-content-center">
            <div class="col-md-6">
                <div>
                    <form class="p-3 p-xl-4" method="post" action="hello-servlet">

                        <div class="mb-3">
                            <label for="dur">code</label>
                            <input class="shadow form-control" type="text" name="code" placeholder="code" id="dur"/>
                        </div>

                        <div><button class="btn btn-primary shadow d-block w-100" type="submit">predire</button></div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>
<jsp:include page="footer.jsp"/>