$(document).ready(function(){
	console.log('main.js loaded');

	window.views.app = new Guisar.Views.App( $('body') );
	window.routers.base = new Guisar.Routers.Base();

	window.ponyExpress = new PonyExpress({
		io : window.location.origin
	});

	window.ponyExpress.bind('connect', function () {
		window.plugs.receta = new PonyExpress.BackbonePlug({
			collection : window.collections.recetas
		});
	});

	// c = new Puls4.Collections.Articles()
	window.collections.recetas = new Guisar.Collections.Recetas();
	window.collections.recetas.on('add', function (model) {
		 console.log('Se agrego un nuevo receta', model.toJSON() );
		// Aqui agregaremos una vista para cada uno de nuesto articulos;
		var view = new Guisar.Views.Receta({model:model});

		view.render();
		$('#listaRecetas').prepend(view.$el.fadeIn());
	});

	var xhr = window.collections.recetas.fetch();

	xhr.done(function(){
		Backbone.history.start({
			root : '/',
			pushState:true
		});
	});
});
